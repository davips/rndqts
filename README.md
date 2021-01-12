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
2021-01-12  102.500000  102.620003  99.330002   99.599998  17608800

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
           Open      High       Low     Close    Volume
Date                                                   
0      0.992071  1.012590  0.974892  0.985990         3
1      1.280855  1.315453  1.028866  1.187199         9
2      1.202997  1.202997  1.160224  1.166542        11
3      1.171458  1.171458  1.153635  1.165728        25
4      1.168232  1.179163  1.162539  1.165955        27
...         ...       ...       ...       ...       ...
34073  1.082212  1.082212  1.054314  1.058348  90423759
34074  1.050895  1.067432  1.050895  1.060755  90423761
34075  1.064736  1.064736  1.035878  1.035878  90423763
34076  1.031813  1.031813  0.984578  0.989224  81846530
34077  1.000000  1.000000  1.000000  1.000000  81846532

[34078 rows x 5 columns]

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

**Fetching from Yahoo** <details>
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
  
