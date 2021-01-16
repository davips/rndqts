# Based on https://code.activestate.com/recipes/496741-object-proxying/

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
from dataclasses import replace

from garoupa import Hash
from pandas import DataFrame


def intercept(self, name, args, kwargs):
    obj = object.__getattribute__(self, "_obj")
    if name in dir(DataFrame):  # and not item.startswith("_"):
        from rndqts.data.lazydataframe import LazyDataFrame
        field = "unevaluated_data" if isinstance(obj, LazyDataFrame) else "data"
        df = getattr(obj, field)
        attribute = getattr(df, name)
        if callable(attribute) or isinstance(attribute, classmethod):
            if args is None:
                return attribute
            val = attribute(*args, **kwargs)
        else:
            val = attribute

        # Handle direct df value.
        if isinstance(val, DataFrame):
            # noinspection PyDataclass
            newquotes = replace(self, _id=Hash(val.to_csv().encode()).id)
            newquotes._data = val
            newquotes.store()
            return newquotes

        # Handle other direct values.
        return val
    attribute = getattr(obj, name)
    return attribute(*args, **kwargs) if callable(attribute) else attribute
    # return attribute(*args, **kwargs) if callable(attribute) or isinstance(attribute, classmethod) else attribute   # loop?


class Proxy:
    """
    Proxy class to intercept magic methods

    Based on https://code.activestate.com/recipes/496741-object-proxying
    """
    __slots__ = ["_obj", "__weakref__"]

    def __init__(self, obj):
        object.__setattr__(self, "_obj", obj)

    #
    # proxying (special cases)
    #
    def __getattribute__(self, name):
        obj = object.__getattribute__(self, "_obj")
        attr = getattr(obj, name)
        if name == '__getitem__':
            return attr
        from rndqts.quotes.abs.quotes import DFWrapper
        if callable(attr) or isinstance(attr, classmethod):
            return DFWrapper(obj, intercept(self, name, None, None))
        else:
            return intercept(self, name, None, None)

    def __delattr__(self, name):
        delattr(object.__getattribute__(self, "_obj"), name)

    def __setattr__(self, name, value):
        setattr(object.__getattribute__(self, "_obj"), name, value)

    def __bool__(self):
        return bool(object.__getattribute__(self, "_obj"))

    def __str__(self):
        return str(object.__getattribute__(self, "_obj"))

    def __repr__(self):
        return repr(object.__getattribute__(self, "_obj"))

    #
    # factories
    #
    _special_names = [
        '__abs__', '__add__', '__and__', '__call__', '__cmp__', '__coerce__',
        '__contains__', '__delitem__', '__delslice__', '__div__', '__divmod__',
        '__eq__', '__float__', '__floordiv__', '__ge__', '__getitem__',
        '__getslice__', '__gt__', '__hex__', '__iadd__', '__iand__',
        '__idiv__', '__idivmod__', '__ifloordiv__', '__ilshift__', '__imod__',
        '__imul__', '__int__', '__invert__', '__ior__', '__ipow__', '__irshift__',
        '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__',
        '__long__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__',
        '__neg__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__',
        '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__',
        '__repr__', '__reversed__', '__rfloorfiv__', '__rlshift__', '__rmod__',
        '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
        '__rtruediv__', '__rxor__', '__setitem__', '__setslice__', '__sub__',
        '__truediv__', '__xor__', 'next',
        # '__hash__'
    ]

    @classmethod
    def _create_class_proxy(cls, theclass):
        """creates a proxy for the given class"""

        def make_method(name):
            def method(self, *args, **kwargs):
                return intercept(self, name, args, kwargs)

            return method

        namespace = {}
        for name_ in cls._special_names:
            if hasattr(theclass, name_) and not hasattr(cls, name_):
                namespace[name_] = make_method(name_)
        return type("%s(%s)" % (cls.__name__, theclass.__name__), (cls,), namespace)

    def __new__(cls, obj, *args, **kwargs):
        """
        creates an proxy instance referencing `obj`. (obj, *args, **kwargs) are
        passed to this class' __init__, so deriving classes can define an
        __init__ method of their own.
        note: _class_proxy_cache is unique per deriving class (each deriving
        class must hold its own cache)
        """
        try:
            cache = cls.__dict__["_class_proxy_cache"]
        except KeyError:
            cls._class_proxy_cache = cache = {}
        try:
            theclass = cache[obj.__class__]
        except KeyError:
            cache[obj.__class__] = theclass = cls._create_class_proxy(obj.__class__)
        ins = object.__new__(theclass)
        # object.__setattr__(ins, "_obj", obj)
        # theclass.__init__(ins, obj, *args, **kwargs)  #commenter said to remove this

        return ins

    def __hash__(self):  # extra
        return hash(object.__getattribute__(self, "_obj"))
