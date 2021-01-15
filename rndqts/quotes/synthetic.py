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

import numpy as np
from dataclasses import replace
import plotly.graph_objects as go

import glob
import math
import os
import pickle
from dataclasses import dataclass

import pandas as pd
import yfinance as yf
from pandas import DataFrame
from rndqts.quotes.abs.quotes import Quotes
from rndqts.data.lazydataframe import LazyDataFrame


@dataclass
class Synthetic(Quotes):
    """
    Pseudo random stock market data.

    Usage:
        >>> from rndqts.quotes.synthetic import Synthetic
        >>> type(Synthetic().data)
        <class 'rndqts.data.lazydataframe.LazyDataFrame'>
        >>> Synthetic()[2]  # doctest: +NORMALIZE_WHITESPACE
        array([  112.22,   117.64,   104.  ,   111.43, 11868.  ])

        >>> Synthetic()[:3].data  # doctest: +NORMALIZE_WHITESPACE
                Open    High     Low   Close  Volume
        Date
        0     112.22  117.64  104.00  111.43   11868
        1     121.24  122.02  100.54  108.78   11689
        2     118.44  124.60  110.35  123.54   12208

    Parameters
    ----------
    seed
        Seed of pseudo random number generator.
    scale
        Standard deviation of Gaussian distribution where variations are sampled.
    varlim_pct
        Threshold in % (e.g., 10) to exclude excessively intense variations when sampling the base data.
    verbosity
        0 - no output; 1 - progress bar
    _slice
        Not intended to be used. Use slicing on the onbject after it is created instead.
    """
    seed: int = 0
    scale: float = 0.1
    varlim_pct: float = 24.99
    verbosity: int = 1
    _slice: slice = None

    _data = None
    _variations = None

    def __post_init__(self):
        super().__init__(self.verbosity, self._slice)

    def _id_(self):
        cfg = f"{self.seed}-{self.varlim_pct}-{self._slice}"
        return hashlib.md5(cfg.encode()).hexdigest()

    @property
    def data(self) -> DataFrame:  # Override to avoid caching and to specialize doctest.
        """
        Date Open High Low Close Volume

        Usage:
            >>> from rndqts.quotes.synthetic import Synthetic
            >>> Synthetic()[:3].data  # doctest: +NORMALIZE_WHITESPACE
                    Open    High     Low   Close  Volume
            Date
            0     112.22  117.64  104.00  111.43   11868
            1     121.24  122.02  100.54  108.78   11689
            2     118.44  124.60  110.35  123.54   12208

        Returns
        -------
        DataFrame
        """
        return self._data_()

    def _data_(self):
        # Random quotes from a seed.
        def newrow(rnd, prev_cl, prev_vl):
            def r():
                val = rnd.normal(scale=self.scale)
                val = val if -lim < val < lim else (-lim if val < 0 else lim)
                return 1 + val

            hilo = [prev_cl * r(), prev_cl * r()]
            hi, lo = max(hilo), min(hilo)
            op, cl = rnd.uniform(lo, hi), rnd.uniform(lo, hi)
            vl = int(math.ceil(prev_vl * r()))
            dic = {}
            dic.update(Open=round(op, 2), High=round(hi, 2), Low=round(lo, 2), Close=round(cl, 2), Volume=vl)
            return dic, cl, vl

        rows = []
        lim = self.varlim_pct / 100
        rnd_ = np.random.RandomState(seed=self.seed)
        c0, v0 = 100, 10000

        # Sliced DataFrame.
        if self._slice.stop != 199999999:
            for i in range(self._slice.start or 0, self._slice.stop, self._slice.step or 1):
                row, c0, v0 = newrow(rnd_, c0, v0)
                rows.append(row)

            df = pd.DataFrame(rows)
            df.index.name = "Date"
            return df

        # Infinite DataFrame.
        return LazyDataFrame(c0, v0, rnd_, newrow)
