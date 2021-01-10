![test](https://github.com/davips/rndqts/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/rndqts/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/rndqts)

# rndqts
Random stock market quotes

**Fetching from Yahoo** <details>
<p>

```python3
from rndqts.quotes import Quotes

print(Quotes("PETR4.sa", progress=False).data)
"""
                 Open       High        Low      Close        Volume
Date                                                                
2000-01-03   4.050103   4.050103   4.050103   4.050103  3.538944e+10
2000-01-04   3.826055   3.826055   3.826055   3.826055  2.886144e+10
2000-01-05   3.787450   3.787450   3.787450   3.787450  4.303360e+10
2000-01-06   3.774351   3.774351   3.774351   3.774351  3.405568e+10
2000-01-07   3.791586   3.791586   3.791586   3.791586  2.091264e+10
...               ...        ...        ...        ...           ...
2021-01-04  28.650000  29.180000  28.530001  28.910000  7.471970e+07
2021-01-05  28.900000  30.180000  28.240000  30.040001  9.518110e+07
2021-01-06  30.160000  30.900000  30.049999  30.100000  9.656250e+07
2021-01-07  30.340000  31.150000  30.340000  31.000000  5.617130e+07
2021-01-08  31.459999  31.760000  30.350000  31.120001  6.713630e+07

[5171 rows x 5 columns]

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
