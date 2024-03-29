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
import hashlib
import math
from dataclasses import dataclass

import pandas as pd
from garoupa import Hash
from pandas import DataFrame

from rndqts.quotes.abs.quotes import Quotes


@dataclass
class Realistic(Quotes):
    """
    Realistic artificial stock market based on real quotes.

    Usage:
        >>> from rndqts import Realistic, Synthetic
        >>> # Replace 'Synthetic(seed=?)[:100]' by any real ticker like 'Real("MSFT")[:100]'.
        >>> base = [Synthetic(seed=1, cached=False)[:100], Synthetic(seed=2, cached=False)[:100]]
        >>> Realistic(base, cached=False)[1]  # doctest: +NORMALIZE_WHITESPACE
        array([  113.84,   113.87,   110.84,   111.95, 10328.  ])

    Parameters
    ----------
    base
        List of Quotes (usually Real) objects to provide data for realistic random quotes generation.
    seed
        Seed of pseudo random number generator for shuffling the variations.
    include_opposite
        Whether to include opposite variations to compensate any long term trending effect contained in the base data.
    varlim_pct
        Threshold in % (e.g., 10) to exclude excessively intense variations when sampling the base data.
    verbosity
        0 - no output; 1 - progress bar
    _slice
        Not intended to be used. Use slicing on the onbject after it is created instead.
    """
    base: list
    seed: int = 0
    include_opposite: int = True
    varlim_pct: float = 24.99
    verbosity: int = 1
    cached: bool = True
    _slice: slice = None
    _id: str = None

    def __post_init__(self):
        base = [qid for qid in sorted(q.id for q in self.base)]
        cfg = f"{base}-{self.seed}-{self.include_opposite}-{self.varlim_pct}-{self._slice}"
        super().__init__(self.verbosity, self.cached, self._slice, self._id or Hash(cfg.encode()).id)

    @property
    def data(self):  # Override just to specialize doctest.
        """
        Date Open High Low Close Volume

        Usage:

        >>> from rndqts import Realistic, Synthetic
        >>> # Replace 'Synthetic(seed=?)[:100]' by any real ticker like 'Real("MSFT")[:100]'.
        >>> base = [Synthetic(seed=1, cached=False)[:100], Synthetic(seed=2, cached=False)[:100]]
        >>> Realistic(base, cached=False).data[:3]  # doctest: +NORMALIZE_WHITESPACE
                Open      High       Low     Close    Volume
        Date
        0     104.43  108.09   99.91  107.24    9749
        1     113.84  113.87  110.84  111.95   10328
        2      99.67  115.47   89.57   96.05   11127

        Returns
        -------

        """
        return super().data

    def _data_(self):
        # Random quotes from real data.  ######################################################################
        def opposite(qs: Quotes):
            qs_op = qs.variations.applymap(lambda a: 1 / a)
            newrows = []
            for idx, row in qs_op.iterrows():
                newrow = dict(row.to_dict())
                newrow["Low"] = row['High']
                newrow["High"] = row['Low']
                newrows.append(newrow)
            df_op = DataFrame(newrows)
            df_op.index.name = "Date"
            return df_op

        # Calculate variations and concatenate all tickers data.
        quotes_objects = self.base
        alldfs = quotes_objects[0].variations
        if self.include_opposite:
            alldfs = alldfs.append(opposite(quotes_objects[0]), ignore_index=True)
        if len(quotes_objects) > 1:
            for quotes in quotes_objects[1:]:
                alldfs = alldfs.append(quotes.variations, ignore_index=True)
                if self.include_opposite:
                    alldfs = alldfs.append(opposite(quotes), ignore_index=True)

        # Remove excessively intense variations and shuffle the remaining ones.
        alldfs = Quotes.limited_variations(alldfs, self.varlim_pct)
        allvariations = alldfs.sample(frac=1, random_state=self.seed).reset_index(drop=True)

        # Generate absolute values starting from $1 and volume 1.
        c0, v0 = 100, 10000
        rows = []
        for o1var, h1var, l1var, c1var, v1var in allvariations.values:
            dic = {}
            v0 = int(math.ceil(v0 * v1var))
            c1 = round(c0 * c1var, 2)
            dic.update(
                Open=round(c0 * o1var, 2), High=round(c0 * h1var, 2), Low=round(c0 * l1var, 2), Close=c1, Volume=v0
            )
            c0 = c1
            rows.append(dic)
        df = pd.DataFrame(rows)
        df.index.name = "Date"
        return df
