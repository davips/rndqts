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
from datetime import datetime, timedelta

import yfinance as yf
from garoupa import Hash

from rndqts.quotes.abs.quotes import Quotes


@dataclass
class Real(Quotes):
    """
    Stock market data from Yahoo Finance.

    Usage:
    >>> Real("MSFT", start="2020-12-20", end="2020-12-31", verbosity=0).data["Volume"]  # doctest: +NORMALIZE_WHITESPACE
    Date
    2020-12-21    37181900
    2020-12-22    22612200
    2020-12-23    18699600
    2020-12-24    10550600
    2020-12-28    17933500
    2020-12-29    17403200
    2020-12-30    20272300
    Name: Volume, dtype: int64

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
    start: str = None
    end: str = None
    calendar_days: int = None
    verbosity: int = 1
    cached: bool = True
    _slice: slice = None
    _id: str = None

    def __post_init__(self):
        if all([self.start, self.end, self.calendar_days]):
            raise Exception("Cannot provide start, end and calendar_days together.")

        # Dumb handling of date intervals.
        if self.start and self.end:
            delta = datetime.strptime(self.end, '%Y-%m-%d') - datetime.strptime(self.start, '%Y-%m-%d')
            self.calendar_days = delta.days
        elif self.start and self.calendar_days:
            delta = timedelta(days=self.calendar_days)
            self.end = (datetime.strptime(self.start, '%Y-%m-%d') + delta).strftime('%Y-%m-%d')
        elif self.end and self.calendar_days:
            delta = timedelta(days=self.calendar_days)
            self.start = (datetime.strptime(self.end, '%Y-%m-%d') - delta).strftime('%Y-%m-%d')
        else:
            if self.calendar_days:
                delta = timedelta(days=self.calendar_days)
                self.end = datetime.today().strftime('%Y-%m-%d')
                self.start = (datetime.strptime(self.end, '%Y-%m-%d') - delta).strftime('%Y-%m-%d')
            elif self.start:
                self.end = datetime.today().strftime('%Y-%m-%d')
                delta = datetime.strptime(self.end, '%Y-%m-%d') - datetime.strptime(self.start, '%Y-%m-%d')
                self.calendar_days = delta.days
            elif self.end:
                self.calendar_days = 14
                delta = timedelta(days=self.calendar_days)
                self.start = (datetime.strptime(self.end, '%Y-%m-%d') - delta).strftime('%Y-%m-%d')
            else:
                self.end = datetime.today().strftime('%Y-%m-%d')
                self.calendar_days = 14
                delta = timedelta(days=self.calendar_days)
                self.start = (datetime.strptime(self.end, '%Y-%m-%d') - delta).strftime('%Y-%m-%d')

        cfg = f"{self.ticker}-{self.start}-{self.end}-{self._slice}"
        super().__init__(self.verbosity, self.cached, self._slice, self._id or Hash(cfg.encode()).id)

    @property
    def data(self):  # Override just to specialize doctest.
        """
        Date Open High Low Close Volume

        Usage:

        >>> from rndqts import Real
        >>> Real("MSFT", start="2021-01-01", calendar_days=7, verbosity=0).data["Volume"]  # doctest: +NORMALIZE_WHITESPACE
        Date
        2021-01-04    37130100
        2021-01-05    23823000
        2021-01-06    35930700
        2021-01-07    27694500
        Name: Volume, dtype: int64

        Returns
        -------

        """
        return super().data

    def _data_(self):
        # Real data.  #########################################################################################
        if self.verbosity > 0:
            print(f"Fetching {self.ticker} ...")
        return yf.download(self.ticker, auto_adjust=True, start=self.start, end=self.end, progress=self.verbosity > 0)
