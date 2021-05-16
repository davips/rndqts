import math
from functools import reduce
from time import sleep

import matplotlib.pyplot as plt
import numpy as np

from rndqts import *

tickers = b3.iloc[:, 0]
# tickers = ["petr4.sa"]
dfs = []
vars = []
# rs = []
for i, ticker in enumerate(tickers):
    r = Real(ticker, start="2001-01-01", end="2020-12-31")
    # rs.append(r)
    dfs.append(r.data)
    vars.append(r.variations)
    sleep(40)

maxi, median, mini = max([len(df) for df in dfs]), np.median([len(df) for df in dfs]), min([len(df) for df in dfs])
print(f"max/median/min: {maxi} / {median} / {mini}")
for lim in [100, 1000, 2000, 4000, 5000]:
    print(f">{lim}:", sum([1 for df in dfs if len(df) > lim]), end="\t\t\t")

allvars = reduce(lambda a, b: a.append(b, ignore_index=True), vars) - 1
print(len(allvars), "candles")


# dfs[0].plot()
# plt.show()

def l(v):
    if abs(v) < 0.0001:
        v = 0
    if v > 0:
        return math.log(2 ** 13 * v, 2)
    elif v < 0:
        return -math.log(2 ** 13 * -v, 2)
    else:
        return 0


def linv(r):
    if r > 0:
        return 2 ** (r - 13.0)
    elif r < 0:
        return -(2 ** (-r - 13.0))
    else:
        return 0


print(allvars.describe())

# allvars = 20 * np.random.random_sample((5, 50)) - 10
allvars = np.vectorize(l)(allvars)
ax = plt.subplot(1, 1, 1)
ax.set_ylim([-17, 18])
ax.boxplot(allvars)
ys = np.arange(-12, 13, 2)
ax.set_xticklabels(dfs[0].keys())
ax.set_yticks(ys)
ax.set_yticklabels([f"{round(linv(y) * 10000) / 100}%" for y in ys])

# allvars.boxplot(column=list(allvars.keys()[:-1]), rot=45, fontsize=15)
print("n:", len(allvars))
plt.show()

#
