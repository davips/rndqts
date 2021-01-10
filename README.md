![test](https://github.com/davips/rndqts/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/rndqts/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/rndqts)

# rndqts
Random stock market quotes

**Fetching from Yahoo** <details>
<p>

```python3
from rndqts.quotes import Quotes

Quotes("PETR4.sa", progress=False).data
"""

"""
```


</p>
</details>

**Random stock quotes** <details>
<p>

```python3
from rndqts.quotes import Quotes

# Caching real quotes from Yahoo.
Quotes("PETR4.sa", progress=False).data
Quotes("VALE3.sa", progress=False).data
Quotes("CSNA3.sa", progress=False).data
Quotes("USIM5.sa", progress=False).data

# Generating random quotes.
random_quotes = Quotes("rnd", seed=42).data.values
print(random_quotes)
"""
[[1.00947569e+00 1.01632731e+00 1.00068496e+00 1.00548117e+00
  3.00000000e+00]
 [1.03308968e+00 1.02043589e+00 1.05266991e+00 1.03492298e+00
  9.00000000e+00]
 [1.04744580e+00 1.03139980e+00 1.06120381e+00 1.03847023e+00
  2.10000000e+01]
 ...
 [4.80039558e+01 4.75309233e+01 4.80039558e+01 4.75395970e+01
  7.81903330e+07]
 [4.67677030e+01 4.73311476e+01 4.65310483e+01 4.65310483e+01
  7.81903350e+07]
 [4.71360374e+01 4.71360374e+01 4.59864740e+01 4.68941008e+01
  5.73796740e+07]]

"""
```

```python3


"""

"""
```


</p>
</details>
