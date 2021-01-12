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
        >>> # Caching a fictitious 'real' ticker for future 'rnd' call.
        >>> Quotes("pseudo").data[:1]  # doctest: +NORMALIZE_WHITESPACE
                 Open      High       Low     Close    Volume
        Date
        0     1.038983  1.168526  0.903264  1.065995       0
        >>> Quotes("rnd", seed=42).data[:3]  # doctest: +NORMALIZE_WHITESPACE
                  Open      High       Low     Close  Volume
        Date
        0     1.200021  1.226008  1.196326  1.202129       5
        1     1.031286  1.338619  0.969459  1.117780      13
        2     1.318694  1.386048  1.054407  1.076145      29

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
    _replace: bool = False
    _data = None

    def __post_init__(self):
        self.scale = float(self.scale)
        none_args = ["start", "end", "n", "seed"]
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

    @cached_property
    def variations(self) -> DataFrame:
        """
        Only variations up to 'lim' are kept.

        Usage:
            >>> from rndqts.quotes import Quotes
            >>> quotes = Quotes("pseudo", n=3)
            >>> quotes.variations
                   Open      High       Low     Close      Volume
            0  0.999654  1.043929  0.976825  1.039087  95181100.0
            1  1.003995  1.028628  1.000333  1.001997  96562500.0
            2  1.007973  1.034884  1.007973  1.029900  56171300.0

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
    def data(self):
        """
        Return Date Open High Low Close Volume

        Usage:
            >>> from rndqts.quotes import Quotes
            >>> # Replace 'pseudo' by any real ticker.
            >>> Quotes("pseudo", n=3).data  # doctest: +NORMALIZE_WHITESPACE
                      Open      High       Low     Close    Volume
            Date
            0     0.986221  1.014387  0.930231  0.933359       0
            1     1.010006  1.039104  0.897452  1.022771       1
            2     1.129749  1.135103  1.037189  1.119618       0
            >>> # Replace 'pseudo' by another real ticker.
            >>> Quotes("pseudo", n=3, seed=42).data  # doctest: +NORMALIZE_WHITESPACE
                      Open      High       Low     Close    Volume
            Date
            0     1.032654  1.049671  0.986174  1.024187       0
            1     1.004030  1.185928  1.000207  1.180340       1
            2     1.146646  1.244380  1.124926  1.146834       1
            >>> Quotes("rnd").data[:5]  # doctest: +NORMALIZE_WHITESPACE
                      Open      High       Low     Close  Volume
            Date
            0     0.933500  0.936102  0.933252  0.933267       5
            1     1.022062  1.027780  0.869450  1.011315      13
            2     0.958251  0.958263  0.953647  0.955773      29
            3     0.944325  0.974614  0.930857  0.936998      61
            4     0.999777  1.002162  0.978533  0.989806     125

        Returns
        -------

        """
        if self._data is None:
            if not os.path.exists('.rndqts'):
                os.makedirs('.rndqts')

            # Look up at the cache.
            args = f"{self.start}§{self.end}§{self.n}§{self.include_opposite}§{self.scale}§{self.lim}§{self.seed}"
            filename = f".rndqts/{self.ticker}§{args}.pickle"
            # if self.ticker != "rnd":
            if os.path.isfile(filename):
                with open(filename, 'rb') as file:
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
                        ticker, start, end, n, rev, scale, lim, seed = f[8:-7].split("§")
                        quotes_objects.append(
                            Quotes(ticker=ticker, start=start, end=end,
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

            # Write to the cache.
            with open(filename, 'wb') as file:
                pickle.dump(self._data, file)

        return self._data

    def save_csv(self, filename=None):
        """
        Usage:
            >>> # Caching for future 'rnd' call.
            >>> Quotes("pseudo").data[:1]  # doctest: +NORMALIZE_WHITESPACE
                     Open      High       Low     Close    Volume
            Date
            0     1.038983  1.168526  0.903264  1.065995       0
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
        >>> quotes = Quotes("pseudo", progress=False)[:5]
        >>> quotes.plot()  # doctest: +SKIP
        """
        df = self.data
        cndstick = go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])
        fig = go.Figure(data=[cndstick])
        fig.show()

    def __getitem__(self, item):
        """Item or slice

        Usage:
        >>> quotes = Quotes("pseudo", progress=False)[:2]
        >>> sliced_quotes = quotes[:2]
        >>> sliced_data = quotes.data[:2]
        >>> all(sliced_quotes == sliced_data)
        True
        """
        newdf = self.data[item]
        if isinstance(newdf, DataFrame):
            n = newdf.shape[0]
            newquotes = replace(self, n=n, _replace=True)
            newquotes._data = newdf
            return newquotes
        return newdf

    def show(self):
        print(self.data)
