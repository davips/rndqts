![test](https://github.com/davips/rndqts/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/rndqts/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/rndqts)

# rndqts
Random stock market quotes


## Installation
### from package
```bash
# Set up a virtualenv. 
python3 -m venv venv
source venv/bin/activate

# Install from PyPI
pip install rndqts
```

### from source
```bash
cd my-project
git clone https://github.com/davips/rndqts ../rndqts
pip install -e ../rndqts
```

## Examples

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
print(Quotes("rnd", seed=42).data)
"""
            Open       High        Low      Close    Volume
Date                                                       
0       1.009476   1.016327   1.000685   1.005481         3
1       1.033090   1.020436   1.052670   1.034923         9
2       1.047446   1.031400   1.061204   1.038470        21
3       1.076301   1.066904   1.117921   1.115601        45
4       1.120012   1.109232   1.140871   1.134210        93
...          ...        ...        ...        ...       ...
36503  48.629245  50.269727  48.066787  48.805014  59063774
36504  47.470540  48.686514  47.159761  47.968600  59063776
36505  48.003956  47.530923  48.003956  47.539597  78190333
36506  46.767703  47.331148  46.531048  46.531048  78190335
36507  47.136037  47.136037  45.986474  46.894101  57379674

[36508 rows x 5 columns]

"""
```

```python3


"""

"""
```


</p>
</details>

**Saving as a CSV file** <details>
<p>

```python3
from rndqts.quotes import Quotes

Quotes("PETR4.sa", progress=False).data.to_csv("/tmp/myfile.csv")


"""

"""
```


</p>
</details>
