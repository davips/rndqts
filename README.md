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

print(Quotes("VALE3.sa").data)
"""
Fetching VALE3.sa ...
[*********************100%***********************]  1 of 1 completed
                  Open        High        Low       Close    Volume
Date                                                               
2000-01-03    2.175114    2.201526   2.175114    2.175114    585600
2000-01-04    2.154401    2.159062   2.123328    2.123328    782400
2000-01-05    2.097431    2.123328   2.097431    2.123328   1876800
2000-01-06    2.123328    2.175114   2.123328    2.123328    792000
2000-01-07    2.149217    2.211886   2.149217    2.201010   5347200
...                ...         ...        ...         ...       ...
2021-01-06   94.980003   96.349998  94.400002   96.050003  53722500
2021-01-07   96.610001  102.529999  96.610001  102.320000  74541400
2021-01-08  103.010002  103.349998  98.199997  101.260002  43879400
2021-01-11  100.250000  101.959999  99.699997  101.800003  18259400
2021-01-12  102.500000  102.620003  99.330002   99.550003  19832500

[5259 rows x 5 columns]

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
Fetching PETR4.sa ...
Fetching CSNA3.sa ...
Fetching USIM5.sa ...
          Open      High       Low     Close    Volume
Date                                                  
0     1.200021  1.226008  1.196326  1.202129         5
1     1.031286  1.338619  0.969459  1.117780        13
2     1.318694  1.386048  1.054407  1.076145        29
3     1.161271  1.337793  0.985241  1.333848        61
4     1.397219  1.412562  1.391739  1.408030       125
...        ...       ...       ...       ...       ...
3995  1.148051  1.161673  1.061298  1.124327  88315543
3996  1.226079  1.253347  1.194810  1.215101  77630090
3997  1.130570  1.137203  1.116103  1.130779  56259184
3998  1.041856  1.105484  0.924760  0.996029  13517372
3999  1.007603  1.008232  0.999234  1.000000  27034747

[4000 rows x 5 columns]

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

Quotes("VALE3.sa").data.to_csv("/tmp/myfile.csv")


"""

"""
```


</p>
</details>

**Plotting** <details>
<p>

```python3
from rndqts.quotes import Quotes

Quotes("VALE3.sa")[1000:1060].plot()
"""
Fetching VALE3.sa ...
[*********************100%***********************]  1 of 1 completed
"""

"""

"""
```


</p>
</details>
![Output as a browser window.](examples/plotvale3.png?raw=true)


## Features / TODO

* [x] Fetch from yahoo
* [x] Automatic local caching
* [x] Slicing
* [x] Plot candle sticks
* [x] Random quotes
       * [x] Ticker 'pseudo' is an option to generate data without real quotes dependence (good for tests)
       * [ ] Explicit real quotes to sample from ('rnd-MSFT,APPL')
       * [ ] 'n' argument fecthes lazily within date interval 
  
