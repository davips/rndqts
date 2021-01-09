import math
import glob
import os
import pickle
from dataclasses import dataclass
from functools import cached_property

import pandas as pd
import yfinance as yf


@dataclass
class Quotes:
    """
    Stock market data for the given ticker, or random quotes based on already accessed real tickers.

    Usage:
        >>> # Caching for future 'rnd' call.
        >>> Quotes("PETR4.sa", progress=False).data[:1]  # doctest: +NORMALIZE_WHITESPACE
                        Open      High       Low     Close        Volume
        Date
        2000-01-03  4.050103  4.050103  4.050103  4.050103  3.538944e+10
        >>> Quotes("rnd", seed=42).data[:3]  # doctest: +NORMALIZE_WHITESPACE
                  Open      High       Low     Close  Volume
        Date
        0     0.993789  1.008568  0.980082  0.991862    1147
        1     0.988887  1.010545  0.978772  1.010545    1109
        2     1.011398  1.018755  1.005210  1.009264    2576

    Parameters
    ----------
        ticker
            Any real ticker (MSFT, PETR4.sa) or the random one (rnd).
    """
    ticker: str
    start: str = None
    end: str = None
    progress: bool = True
    seed: int = None
    include_reverse: int = True

    def __post_init__(self):
        if "None" not in [str(self.start), str(self.end)] and self.ticker == "rnd":
            raise Exception("Only the 'seed' argument is accepted by ticker 'rnd'.", [self.start, self.end])
        if self.seed is not None and self.ticker != "rnd":
            raise Exception("Only 'rnd' ticker can hava a 'seed' argument.", self.seed, self.ticker)
        if self.seed is None:
            self.seed = 0

    @cached_property
    def variations(self):
        """

        Usage:
            >>> from rndqts.rq import Quotes
            >>> quotes = Quotes("PETR4.sa", start="2021-01-01", end="2021-01-8", progress=False)
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
        for i, ((o1, h1, l1, c1, v1), c0, v0) in enumerate(zip(
                self.data.values[1:],
                self.data["Close"].values,
                self.data["Volume"].values
        )):
            dic = {}
            tocheck = [str(math.inf), str(math.nan), str(0.0)]
            if str(c1 / c0) in tocheck:
                c0 = c1 = 1
            if str(v1 / v0) in tocheck:
                v0 = v1 = 1
            dic.update(Date=i+1, Open=o1 / c0, High=h1 / c0, Low=l1 / c0, Close=c1 / c0, Volume=v1 / v0)
            rows.append(dic)
        return pd.DataFrame(rows)

    @cached_property
    def data(self):
        """
        Return Date Open High Low Close Volume

        Usage:
            >>> from rndqts.rq import Quotes
            >>> Quotes("PETR4.sa", start="2021-01-01", end="2021-01-8", progress=False).data  # doctest: +NORMALIZE_WHITESPACE
                         Open   High        Low      Close    Volume
            Date
            2021-01-04  28.65  29.18  28.530001  28.910000  74719700
            2021-01-05  28.90  30.18  28.240000  30.040001  95181100
            2021-01-06  30.16  30.90  30.049999  30.100000  96562500
            2021-01-07  30.34  31.15  30.340000  31.000000  56171300

        Returns
        -------

        """
        if not os.path.exists('.rndqts'):
            os.makedirs('.rndqts')

        # Look up at the cache.
        filename = f".rndqts/{self.ticker}§{self.start}§{self.end}§{self.seed}.pickle"
        if self.ticker != "rnd":
            if os.path.isfile(filename):
                with open(filename, 'rb') as file:
                    return pickle.load(file)

        # Fetch/generate data.
        if self.ticker == "rnd":
            # Random quotes from real data.
            files = glob.glob('.rndqts/*.pickle')
            if len(files) == 0:
                raise Exception("Cannot generate random quotes without caching real quotes first.")

            quotes_objects = []
            for f in files:
                if "rnd§" not in f:
                    ticker, start, end, _ = f[8:-7].split("§")
                    quotes_objects.append(Quotes(ticker=ticker, start=start, end=end))

            # Calculate variations and concatenate all tickers.
            alldfs = quotes_objects[0].variations
            if len(quotes_objects) > 1:
                for quotes in quotes_objects[1:]:
                    alldfs = alldfs.append(quotes.variations, ignore_index=True)
                    alldfs = alldfs.append(quotes.variations.applymap(lambda a: 1 / a), ignore_index=True)

            # Shuffle variations.
            allvariations = alldfs.sample(frac=1, random_state=self.seed).reset_index(drop=True)

            # Generate absolute values starting from $1 and volume 1.
            c0 = 1
            v0 = 1
            rows = []
            for d1, o1, h1, l1, c1, v1 in allvariations.values:
                dic = {}
                try:
                    vol = int((int(v0) * int(v1)) % 99000999)
                    dic.update(Open=c0 * o1, High=c0 * h1, Low=c0 * l1, Close=c0 * c1, Volume=vol)
                except:
                    raise Exception(v0, v1)
                rows.append(dic)
                c0 *= c1
                v0 = vol
            df = pd.DataFrame(rows)
            df.index.name = "Date"
        else:
            # Real data.
            df = yf.download(self.ticker, auto_adjust=True, start=self.start, end=self.end, progress=self.progress)

        # Write to the cache.
        with open(filename, 'wb') as file:
            pickle.dump(df, file)

        return df

    def save_csv(self, filename=None):
        """
        Usage:
            >>> # Caching for future 'rnd' call.
            >>> Quotes("PETR4.sa", progress=False).data[:1]  # doctest: +NORMALIZE_WHITESPACE
                            Open      High       Low     Close        Volume
            Date
            2000-01-03  4.050103  4.050103  4.050103  4.050103  3.538944e+10
            >>> quotes = Quotes("rnd", seed=42)
            >>> quotes.save_csv("/run/shm/rndqts-doctest.csv")
            >>> quotes.save_csv()  # Default name: PETR4.sa_2021-01-01_2021-01-8_0.csv.

        Parameters
        ----------
        filename

        Returns
        -------

        """
        if filename is None:
            filename = f"{self.ticker}_{self.start}_{self.end}_{self.seed}.csv"
        return self.data.to_csv(filename)
