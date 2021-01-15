#  Copyright (c) 2021. Davi Pereira dos Santos
#  This file is part of the rndqts project.
#  Please respect the license - more about this in the section (*) below.
#
#  rndqts is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  rndqts is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with rndqts.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.
#  Relevant employers or funding agencies will be notified accordingly.
from dataclasses import dataclass

import pandas as pd
from numpy.random import RandomState
import numpy as np

@dataclass
class LazyDataFrame:
    prev_close: float
    prev_volume: float
    rnd:RandomState
    func: callable

    @staticmethod
    def _tip(item):
        return f"compatible with lazy/infinite data.\n" \
               f"Please slice this LazyDataFrame before accessing pandas features, e.g.:\n" \
               f"lazydf[:100]{item}"

    def __getattr__(self, item):
        """
        Usage:
            >>> from rndqts.quotes.synthetic import Synthetic
            >>> Synthetic().data[:3].count()
            Open      3
            High      3
            Low       3
            Close     3
            Volume    3
            dtype: int64

            >>> try:
            ...     Synthetic().data.count()
            ... except Exception as e:
            ...     print(e)  # doctest: +NORMALIZE_WHITESPACE
            LazyDataFrame error:
            The pandas feature <count> may be implemented in the future if it is  compatible with lazy/infinite data.
            Please slice this LazyDataFrame before accessing pandas features, e.g.:
            lazydf[:100].count

        Parameters
        ----------
        item

        Returns
        -------

        """
        if item in dir(pd.DataFrame) and not item.startswith("_"):
            msg = self._tip("." + item)
            raise Exception(f"LazyDataFrame error:\n"
                            f"The pandas feature <{item}> may be implemented in the future if it is {msg}")
        return super().__getattribute__(item)

    def __getitem__(self, item):
        direct = False
        if isinstance(item, slice):
            if item.stop is None:
                raise Exception(f"Ths slice {item} will never end.")
            start, stop, step = item.start or 0, item.stop, item.step or 1
        elif isinstance(item, int):
            start, stop, step = 0, item + 1, 1
            direct = True
        else:
            msg = self._tip("[" + str(item) + "]")
            raise Exception(f"LazyDataFrame error:\nPandas-like access to columns is not {msg}")

        rows = []
        row = None
        c0, v0 = self.prev_close, self.prev_volume
        for i in range(start, stop, step):
            row, c0, v0 = self.func(self.rnd, c0, v0)
            if not direct:
                rows.append(row)
        if direct:
            if row is None:
                raise Exception(f"Wrong index: {item}")
            return np.array(list(row.values()))

        df = pd.DataFrame(rows)
        df.index.name = "Date"
        return df
