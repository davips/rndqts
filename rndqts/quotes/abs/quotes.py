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
import glob
import math
import os
import pickle
import warnings
from abc import ABC, abstractmethod
from dataclasses import replace, dataclass
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
from garoupa import Hash
from garoupa.decorator import classproperty
from pandas import DataFrame


class Quotes(ABC):
    """Base-class for different types of quote generators."""
    _data = None
    _appdir = None

    def __init__(self, verbosity: int, cached: bool, _slice: slice, _id: str):
        self.verbosity = verbosity
        self.cached = True if cached is None else cached
        _slice = _slice or slice(199999999)
        self._slice = slice(_slice.start or 0, _slice.stop, _slice.step or 1)
        self.id = _id
        self.filename = f"{self.appdir}/{self.id}.pickle"
        self._variations = None

    @classproperty
    def appdir(self):
        if self._appdir is None:
            self._appdir = f"{str(Path.home())}/.rndqts"
            if not os.path.exists(self.appdir):
                # Create app data dir if inexistent.
                os.makedirs(self.appdir)
        return self._appdir

    @property
    def data(self) -> DataFrame:
        if self._data is None:
            if self.cached:
                # Return cached data if any.
                if os.path.isfile(self.filename):
                    with open(self.filename, 'rb') as file:
                        try:
                            self._data = pickle.load(file)
                        except Exception as e:
                            raise Exception(self.filename, e)
                        return self._data

            # Generate data and cache it.
            self._data = self._data_()
            if self.cached:
                self.store()

        return self._data

    @abstractmethod
    def _data_(self):
        pass

    @property
    def variations(self) -> DataFrame:
        """
        n-1 variations between n days.

        5% variation is shown here as 1.05

        Usage:
            >>> from rndqts.quotes.synthetic import Synthetic
            >>> quotes = Synthetic(cached=False)[:3]
            >>> quotes.variations  # doctest: +NORMALIZE_WHITESPACE
                      Open      High       Low     Close    Volume
            Date
            0     1.088037  1.095037  0.902270  0.976218  0.984917
            1     1.088803  1.145431  1.014433  1.135687  1.044401

        Returns
        -------
            DataFrame containg the variations of open, high, low and close when compared to the previous 'close'.
        """
        if self._variations is None:
            rows = []
            for (o1, h1, l1, c1, v1), c0, v0 in \
                    zip(self.data.values[1:], self.data["Close"].values, self.data["Volume"].values):
                dic = {}
                tocheck = [str(math.inf), str(math.nan), str(0.0)]

                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", RuntimeWarning)
                    if str(c1 / c0) in tocheck:
                        c0 = c1 = 1
                    if str(v1 / v0) in tocheck:
                        v0 = v1 = 1
                dic.update(Open=o1 / c0, High=h1 / c0, Low=l1 / c0, Close=c1 / c0, Volume=v1 / v0)
                rows.append(dic)
            self._variations = pd.DataFrame(rows)
            self._variations.index.name = "Date"
        return self._variations

    def store(self):
        """Write data to the local cache."""
        with open(self.filename, 'wb') as file:
            pickle.dump(self._data, file)

    def save_csv(self, filename=None):
        """
        Usage:
            >>> from rndqts.quotes.synthetic import Synthetic
            >>> quotes = Synthetic(seed=42, cached=False)[:1000]
            >>> quotes.save_csv("/run/shm/rndqts-doctest.csv")

            >>> # Default name: pseudo_None_None_42.csv.
            >>> quotes.save_csv()  # doctest: +SKIP

        Parameters
        ----------
        filename
            Default: Quotes object id

        Returns
        -------

        """
        if filename is None:
            filename = f"{self.filename[8:-7]}.csv"
        return self.data.to_csv(filename)

    def plot(self):  # pragma: no cover
        """Item or slice

        Usage:
        >>> from rndqts.quotes.synthetic import Synthetic
        >>> quotes = Synthetic(seed=42, cached=False)[:60]
        >>> quotes.plot()  # doctest: +SKIP
        """
        df = self.data
        cndstick = go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])
        fig = go.Figure(data=[cndstick])
        fig.show()

    def __iter__(self):
        """
        Usage:
            >>> from rndqts.quotes.synthetic import Synthetic
            >>> for row in Synthetic(cached=False)[:2]:
            ...     print(row)
            [  112.22   117.64   104.     111.43 11868.  ]
            [  121.24   122.02   100.54   108.78 11689.  ]

        Returns
        -------

        """
        yield from self.data.to_numpy()

    def __getitem__(self, item):
        """Item or slice

        Usage:
            >>> from rndqts.quotes.synthetic import Synthetic
            >>> list(Synthetic(cached=False)[:2])
            [array([  112.22,   117.64,   104.  ,   111.43, 11868.  ]), array([  121.24,   122.02,   100.54,   108.78, 11689.  ])]

            >>> print(Synthetic(cached=False)[1])
            [  112.22   117.64   104.     111.43 11868.  ]
        """

        if isinstance(item, slice):
            if item.stop is None:
                raise Exception(f"Ths slice {item} will never end.")
            # noinspection PyDataclass
            newquotes = replace(self, _slice=item, _id=None)
            newquotes._data = self.data[item]
            if newquotes.cached:
                newquotes.store()
            return newquotes
        elif isinstance(item, int):
            return list(self[item:item + 1])[0]
        return self.data[item]

    def show(self):
        """
        Usage:
            >>> from rndqts.quotes.synthetic import Synthetic
            >>> Synthetic(cached=False)[:5].show()  # doctest: +NORMALIZE_WHITESPACE
                       Open       High        Low      Close   Volume
            Date
            0     112.22  117.64  104.00  111.43   11868
            1     121.24  122.02  100.54  108.78   11689
            2     118.44  124.60  110.35  123.54   12208
            3     129.35  141.99  127.66  136.83   11958
            4     114.05  145.78  102.64  136.04   14673

        Returns
        -------

        """
        print(self.data)

    @classmethod
    def cached_items(cls):
        """Generator cantaining all cached Quotes objects"""
        files = glob.glob(f"{cls.appdir}/*.pickle")
        for f in files:
            with open(f, 'rb') as file:
                yield pickle.load(file)

    @staticmethod
    def limited_variations(variations: DataFrame, varlim_pct: float):
        """Remove excessively intense variations"""
        lim = varlim_pct / 100 + 1
        return variations.applymap(lambda a: a if -lim < a < lim else -lim if a < 0 else lim)

    def __getattr__(self, item):
        """Redirect any pandas attribute to self.data"""
        # TODO: __add__ etc. (through pandas or manually)
        if item in dir(pd.DataFrame):  # and not item.startswith("_"):
            attribute = getattr(self.data, item)

            # Handle methods.
            if callable(attribute) or isinstance(attribute, classmethod):
                return DFWrapper(self, attribute)

            # Handle direct df value.
            if isinstance(attribute, DataFrame):
                # noinspection PyDataclass
                newquotes = replace(self, _id=Hash(attribute.to_csv().encode()).id)
                newquotes._data = attribute
                if newquotes.cached:
                    newquotes.store()
                return newquotes

            # Handle other direct values.
            return attribute

        print(item)
        return super().__getattribute__(item)


@dataclass
class DFWrapper:
    quotes: Quotes
    attribute: callable

    def __call__(self, *args, **kwargs):
        val = self.attribute(*args, **kwargs)
        if isinstance(val, DataFrame):
            # noinspection PyDataclass
            newquotes = replace(self.quotes, _id=Hash(val.to_csv().encode()).id)
            newquotes._data = val
            if newquotes.cached:
                newquotes.store()
            return newquotes
