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


@dataclass
class Real(Quotes):
    """
    Stock market data from Yahoo Finance.

    Usage:
    >>> Real("MSFT", start="2020-12-20", end="2020-12-31", verbosity=0).data  # doctest: +NORMALIZE_WHITESPACE
                      Open        High         Low       Close    Volume
    Date
    2020-12-21  217.550003  224.000000  217.279999  222.589996  37181900
    2020-12-22  222.690002  225.630005  221.850006  223.940002  22612200
    2020-12-23  223.110001  223.559998  220.800003  221.020004  18699600
    2020-12-24  221.419998  223.610001  221.199997  222.750000  10550600
    2020-12-28  224.449997  226.029999  223.020004  224.960007  17933500
    2020-12-29  226.309998  227.179993  223.580002  224.149994  17403200
    2020-12-30  225.229996  225.630005  221.470001  221.679993  20272300

    Parameters
    ----------
    ticker
                Any real ticker (MSFT, VALE3.sa, ...).
    start
        Initial date in the format 'yyyy-mm-dd'.
    end
        End date in the format 'yyyy-mm-dd'.
    verbosity
        0 - no output; 1 - progress bar
    _slice
        Not intended to be used. Use slicing on the onbject after it is created instead.
    """
    ticker: str
    start: str = "2020-12-01"
    end: str = "2020-12-31"
    verbosity: int = 1
    _slice: slice = None

    def __post_init__(self):
        super().__init__(self.verbosity, self._slice)

    def _id_(self):
        cfg = f"{self.ticker}-{self.start}-{self.end}-{self._slice}"
        return hashlib.md5(cfg.encode()).hexdigest()

    @property
    def data(self):  # Override just to specialize doctest.
        """
        Date Open High Low Close Volume

        Usage:

        >>> from rndqts import Realistic, Synthetic
        >>> # Replace 'Synthetic(seed=?)[:100]' by any real ticker like 'Real("MSFT")[:100]'.
        >>> base = [Synthetic(seed=1)[:100], Synthetic(seed=2)[:100]]
        >>> Realistic(base).data[:3]  # doctest: +NORMALIZE_WHITESPACE
                    Open        High         Low       Close  Volume
        Date
        0     104.43  108.09   99.91  107.24    9749
        1     113.84  113.87  110.84  111.95   10328
        2      99.67  115.47   89.57   96.05   11127

        Returns
        -------

        """
        return super().data

    def _data_(self):
        # Real data.  #########################################################################################
        if self.verbosity > 0:
            print(f"Fetching {self.ticker} ...")
        return yf.download(self.ticker, auto_adjust=True, start=self.start, end=self.end, progress=self.verbosity > 0)
