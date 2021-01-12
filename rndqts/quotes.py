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
        0     1.35281  1.448179  1.080031  1.195748  74753034
        >>> Quotes("rnd", seed=42).data[:3]  # doctest: +NORMALIZE_WHITESPACE
                  Open      High       Low     Close  Volume
        Date
        0     0.941916  0.806452  1.380485  1.054535       3
        1     0.864990  1.286075  0.829096  0.945686       9
        2     0.896303  0.936274  0.725149  0.863001      11

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
    include_reverse: int = True
    scale: float = 0.2
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
    def variations(self):
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
            >>> Quotes("pseudo",n=3).data  # doctest: +NORMALIZE_WHITESPACE
                      Open      High       Low     Close    Volume
            Date
            0     1.352810  1.448179  1.080031  1.195748  74753034
            1     1.074767  1.666854  0.994211  1.498539  48220335
            2     1.835805  1.864365  1.097082  1.390945  86414068
            >>> # Replace 'pseudo' by another real ticker.
            >>> Quotes("pseudo", n=3, seed=42).data  # doctest: +NORMALIZE_WHITESPACE
                      Open      High       Low     Close    Volume
            Date
            0     1.352810  1.448179  1.080031  1.195748  74753034
            1     1.074767  1.666854  0.994211  1.498539  48220335
            2     1.835805  1.864365  1.097082  1.390945  86414068
            >>> Quotes("rnd").data[:5]  # doctest: +NORMALIZE_WHITESPACE
                      Open      High       Low     Close  Volume
            Date
            0     1.225063  1.240000  0.732101  0.928201       5
            1     1.032683  0.748549  1.116357  0.748549      13
            2     0.917020  0.928201  0.548013  0.694804      29
            3     0.624507  0.861557  0.577698  0.861557      31
            4     0.703276  0.694804  1.176828  0.928201      33

        Returns
        -------

        """
        if self._data is None:
            if not os.path.exists('.rndqts'):
                os.makedirs('.rndqts')

            # Look up at the cache.
            args = f"{self.start}§{self.end}§{self.n}§{self.include_reverse}§{self.scale}§{self.lim}§{self.seed}"
            filename = f".rndqts/{self.ticker}§{args}.pickle"
            # if self.ticker != "rnd":
            if os.path.isfile(filename):
                with open(filename, 'rb') as file:
                    self._data = pickle.load(file)
                    return self._data

            # Fetch/generate data.
            if self.ticker == "pseudo":
                # Random quotes from a seed.  #########################################################################
                rnd = np.random.RandomState(seed=0)  # rnd = np.random.default_rng(seed)
                rows = []
                r = lambda: 1 + rnd.normal(scale=self.scale)
                c0, v0 = 1, 1
                n = 0 if self.n is None else self.n
                for i in range(max(1000, n)):
                    o1, h1, l1, c1, v1 = r(), r(), r(), r(), rnd.random_integers(1, 100000000)
                    dic = {}
                    dic.update(Open=c0 * o1, High=c0 * h1, Low=c0 * l1, Close=c0 * c1)
                    s = sorted(dic.values())
                    dic["High"] = s[-1]
                    dic["Low"] = s[0]
                    dic["Open"] = rnd.choice([s[1], s[2]])
                    c0 = dic["Close"] = s[2] if s[2] != dic["Open"] else s[1]
                    dic.update(Volume=v0 * v1)
                    rows.append(dic)
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
                                   n=n, include_reverse=bool(rev), scale=scale, lim=float(lim))
                        )

                # Calculate variations and concatenate all tickers.
                alldfs = quotes_objects[0].variations
                if self.include_reverse:
                    alldfs = alldfs.append(quotes_objects[0].variations.applymap(lambda a: 1 / a), ignore_index=True)
                if len(quotes_objects) > 1:
                    for quotes in quotes_objects[1:]:
                        alldfs = alldfs.append(quotes.variations, ignore_index=True)
                        if self.include_reverse:
                            alldfs = alldfs.append(quotes.variations.applymap(lambda a: 1 / a), ignore_index=True)

                # Shuffle variations.
                allvariations = alldfs.sample(frac=1, random_state=self.seed).reset_index(drop=True)

                # Generate absolute values starting from $1 and volume 1.
                c0 = 1
                v0 = 1
                rows = []
                for o1, h1, l1, c1, v1 in allvariations.values:
                    dic = {}
                    try:
                        vol = int(((int(v0 + 1) * int(v1 + 1)) + 1) % 99000999)
                        dic.update(Open=c0 * o1, High=c0 * h1, Low=c0 * l1, Close=c0 * c1)
                        # dic["High"] = max(dic.values())
                        # dic["Low"] = min(dic.values())
                        dic.update(Volume=vol)
                    except:
                        raise Exception(v0, v1)
                    rows.append(dic)
                    c0 *= c1
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
            >>> Quotes("pseudo", progress=False).data[:1]  # doctest: +NORMALIZE_WHITESPACE
                     Open      High       Low     Close    Volume
            Date
            0     1.35281  1.448179  1.080031  1.195748  74753034
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
