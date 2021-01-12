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

import numpy as np
from dataclasses import replace
import plotly.graph_objects as go

import glob
import math
import os
import pickle
from dataclasses import dataclass
from functools import cached_property

import pandas as pd
import yfinance as yf
from pandas import DataFrame


@dataclass
class Quotes:
    """
    Stock market data for the given ticker, or random quotes.
        'rnd':          based on real tickers and a shuffling seed
        'pseudo':    just based on a seed

    Usage:
        >>> Quotes("pseudo").data[:1]  # doctest: +NORMALIZE_WHITESPACE
                 Open      High       Low     Close    Volume
        Date
        0     1.047819  1.064518  0.851965  0.971409       1

    Parameters
    ----------
        ticker
            Any real ticker (MSFT, VALE3.sa) or the random one (rnd).
    """
    ticker: str
    start: str = None
    end: str = None
    progress: bool = True
    n: int = None
    lim: float = 24
    seed: int = None
    include_opposite: int = True
    scale: float = 0.1
    slice: str = None
    _replace: bool = False
    _data = None

    def __post_init__(self):
        self.scale = float(self.scale)
        none_args = ["start", "end", "n", "seed", "slice"]
        for arg in none_args:
            if getattr(self, arg) == "None":
                setattr(self, arg, None)
        if self.n is not None:
            self.n = int(self.n)

        if not self._replace:
            random = (self.ticker.startswith("rnd") or self.ticker.startswith("pseudo"))
            if "None" not in [str(self.start), str(self.end)] and random:
                raise Exception("Only the 'seed' argument is accepted by ticker 'rnd'.", [self.start, self.end])
            if self.seed is not None and not random:
                raise Exception("Only the 'rnd' ticker can have a 'seed' argument.", self.seed, self.ticker)
        args = f"{self.start}§{self.end}§{self.n}§{self.include_opposite}§{self.scale}§{self.lim}§{self.slice}"
        self.filename = f".rndqts/{self.ticker}§{args}§{self.seed}.pickle"

    @cached_property
    def variations(self) -> DataFrame:
        """
        Only variations up to 'lim' are kept.

        Usage:
            >>> from rndqts.quotes import Quotes
            >>> quotes = Quotes("pseudo", n=3)
            >>> quotes.variations  # doctest: +NORMALIZE_WHITESPACE
                   Open      High       Low     Close      Volume
            Date
            0     1.012494  1.031401  0.996855  1.008132     1.0
            1     0.987351  1.014483  0.977188  0.991337     1.0

        Parameters
        ----------
        quotes

        Returns
        -------
            DataFrame containg the variation when compared to the previous 'close'.
        """
        rows = []
        for (o1, h1, l1, c1, v1), c0, v0 in \
                zip(self.data.values[1:], self.data["Close"].values, self.data["Volume"].values):
            dic = {}
            tocheck = [str(math.inf), str(math.nan), str(0.0)]
            if str(c1 / c0) in tocheck:
                c0 = c1 = 1
            if str(v1 / v0) in tocheck:
                v0 = v1 = 1
            dic.update(Open=o1 / c0, High=h1 / c0, Low=l1 / c0, Close=c1 / c0, Volume=v1 / v0)
            rows.append(dic)
        df = pd.DataFrame(rows)
        df.index.name = "Date"
        lim = self.lim / 100 + 1
        return df.applymap(lambda a: a if -lim < a < lim else -lim if a < 0 else lim)

    @property
    def data(self):  # TODO: Add example for 'rnd' and 'EXAMPLETICKER'
        """
        Return Date Open High Low Close Volume

        Usage:
            >>> from rndqts.quotes import Quotes
            >>> # Replace 'pseudo' by any real ticker.
            >>> Quotes("pseudo", n=3).data  # doctest: +NORMALIZE_WHITESPACE
                      Open      High       Low     Close    Volume
            Date
            0     0.791850  0.908542  0.767585  0.876627       0
            1     0.688895  0.773534  0.632679  0.717124       0
            2     0.683110  0.806367  0.558580  0.662190       1

        Returns
        -------

        """
        if self._data is None:
            if not os.path.exists('.rndqts'):
                os.makedirs('.rndqts')

            # Look up at the cache.
            if os.path.isfile(self.filename):
                with open(self.filename, 'rb') as file:
                    self._data = pickle.load(file)
                    return self._data

            # Fetch/generate data.
            if self.ticker == "pseudo":
                # Random quotes from a seed.  #########################################################################
                rnd = np.random.RandomState(seed=self.seed)
                rows = []
                r = lambda: abs(1 + rnd.normal(scale=self.scale))
                c0, v0 = 1, 1
                n = 0 if self.n is None else self.n
                for i in range(max(1000, n)):
                    hilo = [c0 * r(), c0 * r()]
                    hi, lo = max(hilo), min(hilo)
                    op, cl = rnd.uniform(lo, hi), rnd.uniform(lo, hi)
                    vl = int(v0 * r())
                    dic = {}
                    dic.update(Open=op, High=hi, Low=lo, Close=cl, Volume=vl)
                    rows.append(dic)
                    c0 = cl
                df = pd.DataFrame(rows)
                df.index.name = "Date"
            elif self.ticker == "rnd":
                # Random quotes from real data.  ######################################################################
                files = glob.glob('.rndqts/*.pickle')
                if len(files) == 0:
                    raise Exception("Cannot generate random quotes without caching real or pseudornd quotes first.")

                quotes_objects = []
                for f in files:
                    if "rnd§" not in f:
                        ticker, start, end, n, rev, scale, lim, slic, seed = f[8:-7].split("§")
                        quotes_objects.append(
                            Quotes(ticker=ticker, start=start, end=end, slice=slic,
                                   n=n, include_opposite=bool(rev), scale=scale, lim=float(lim))
                        )

                def opposite(qs: Quotes):
                    qs_op = qs.variations.applymap(lambda a: 1 / a)
                    newrows = []
                    for idx, row in qs_op.iterrows():
                        newrow = row.to_dict()
                        if row['High'] < row['Low']:
                            newrow["Low"] = row['High']
                            newrow["High"] = row['Low']
                        newrows.append(newrow)
                    df_op = DataFrame(newrows)
                    df_op.index.name = "Date"
                    return df_op

                # Calculate variations and concatenate all tickers.
                alldfs = quotes_objects[0].variations
                if self.include_opposite:
                    # alldfs = opposite(quotes_objects[0])
                    alldfs = alldfs.append(opposite(quotes_objects[0]), ignore_index=True)
                if len(quotes_objects) > 1:
                    for quotes in quotes_objects[1:]:
                        alldfs = alldfs.append(quotes.variations, ignore_index=True)
                        if self.include_opposite:
                            alldfs = alldfs.append(opposite(quotes), ignore_index=True)

                # Shuffle variations.
                allvariations = alldfs.sample(frac=1, random_state=self.seed).reset_index(drop=True)

                # Generate absolute values starting from $1 and volume 1.
                c0 = 1
                v0 = 1
                rows = []
                for o1var, h1var, l1var, c1var, v1var in allvariations.values:
                    dic = {}
                    try:
                        vol = int(((int(v0 + 1) * int(v1var + 1)) + 1) % 99000999)
                        dic.update(Open=c0 * o1var, High=c0 * h1var, Low=c0 * l1var, Close=c0 * c1var)
                        dic.update(Volume=vol)
                    except:
                        raise Exception(v0, v1var)
                    rows.append(dic)
                    c0 *= c1var
                    v0 = vol
                df = pd.DataFrame(rows)
                df.index.name = "Date"
            else:
                # Real data.  #########################################################################################
                print(f"Fetching {self.ticker} ...")
                df = yf.download(self.ticker, auto_adjust=True, start=self.start, end=self.end, progress=self.progress)

            self._data = df if self.n is None else df[:self.n]
            self.store()

        return self._data

    def store(self):
        """Write data to the local cache."""
        with open(self.filename, 'wb') as file:
            pickle.dump(self._data, file)

    def save_csv(self, filename=None):
        """
        Usage:
            >>> quotes = Quotes("pseudo", seed=42)
            >>> quotes.save_csv("/run/shm/rndqts-doctest.csv")
            >>> quotes.save_csv()  # Default name: pseudo_None_None_42.csv.

        Parameters
        ----------
        filename

        Returns
        -------

        """
        if filename is None:
            filename = f"{self.ticker}_{self.start}_{self.end}_{self.seed}.csv"
        return self.data.to_csv(filename)

    def plot(self):  # pragma: no cover
        """Item or slice

        Usage:
        >>> quotes = Quotes("pseudo")[:5]
        >>> quotes.plot()  # doctest: +SKIP
        """
        df = self.data
        cndstick = go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])
        fig = go.Figure(data=[cndstick])
        fig.show()

    def __getitem__(self, item):
        """Item or slice

        Usage:
        >>> quotes = Quotes("pseudo")[:2]
        >>> sliced_quotes = quotes[:2]
        >>> sliced_data = quotes.data[:2]
        >>> all(sliced_quotes == sliced_data)
        True
        """
        newdf = self.data[item]
        if isinstance(newdf, DataFrame):
            n = newdf.shape[0]
            newquotes = replace(self, slice=str(item).replace(" ", "-"), n=n, _replace=True)
            newquotes._data = newdf
            newquotes.store()
            return newquotes
        return newdf

    def show(self):
        """
        Usage:
            >>> Quotes("pseudo")[:5].show()  # doctest: +NORMALIZE_WHITESPACE
                      Open      High       Low     Close  Volume
            Date
            0     1.047819  1.064518  0.851965  0.971409       1
            1     0.911649  1.038649  0.905199  0.994486       0
            2     1.033183  1.052464  0.923934  0.935493       1
            3     0.841302  0.889959  0.837215  0.861448       1
            4     0.843304  0.878349  0.806405  0.816766       0

        Returns
        -------

        """
        print(self.data)
