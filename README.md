![test](https://github.com/davips/rndqts/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/rndqts/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/rndqts)

# rndqts
Random stock market quotes

<img src="https://raw.githubusercontent.com/davips/rndqts/main/examples/chart.png" alt="Output as a browser window" width="200" height="200">

[Latest version](https://github.com/davips/rndqts)

## Installation
### as a standalone lib.
```bash
# Set up a virtualenv. 
python3 -m venv venv
source venv/bin/activate

# Install from PyPI...
pip install --upgrade pip
pip install -U rndqts

# ...or, install from updated source code.
pip install git+https://github.com/davips/rndqts
```

### as an editable lib inside your project.
```bash
cd your-project
source venv/bin/activate
git clone https://github.com/davips/rndqts ../rndqts
pip install --upgrade pip
pip install -e ../rndqts
```

## Examples

**Fetching from Yahoo**
<details>
<p>

```python3
from rndqts import Real

print(Real("VALE3.sa").data)
"""
Fetching VALE3.sa ...
[*********************100%***********************]  1 of 1 completed
                 Open       High        Low      Close    Volume
Date                                                            
2020-12-01  79.830002  81.500000  79.250000  81.250000  61441200
2020-12-02  80.900002  81.250000  77.309998  79.839996  53703300
2020-12-03  81.000000  81.050003  78.610001  78.959999  35158600
2020-12-04  80.099998  82.680000  80.099998  82.269997  38441000
2020-12-07  82.419998  82.989998  81.669998  82.949997  27398500
2020-12-08  82.970001  83.300003  81.660004  82.900002  28598800
2020-12-09  83.099998  83.830002  82.220001  82.699997  26938500
2020-12-10  83.650002  85.220001  83.199997  85.000000  41230700
2020-12-11  84.620003  85.279999  84.400002  84.760002  17825100
2020-12-14  85.199997  85.220001  82.949997  83.550003  20931700
2020-12-15  83.550003  85.379997  83.550003  84.500000  18762800
2020-12-16  84.900002  86.230003  84.360001  86.220001  23038300
2020-12-17  86.500000  87.949997  86.169998  87.199997  21367800
2020-12-18  87.620003  88.349998  87.430000  88.190002  13534400
2020-12-21  86.150002  87.400002  84.779999  86.860001  31877300
2020-12-22  86.860001  86.989998  85.430000  86.940002  23157000
2020-12-23  86.529999  87.529999  86.400002  87.360001  17710200
2020-12-28  87.790001  88.580002  87.080002  87.309998  26001300
2020-12-29  87.970001  88.199997  86.510002  87.070000  19727500
2020-12-30  87.190002  87.589996  86.650002  87.449997  30102700
"""
```


</p>
</details>

**Random stock quotes**
<details>
<p>

```python3
from rndqts import Realistic
from rndqts import Real

# Real quotes to fetch from Yahoo.
r1 = Real("PETR4.sa")
r2 = Real("CSNA3.sa")
r3 = Real("VALE3.sa")
r4 = Real("USIM5.sa")

# Generating random quotes.
print(Realistic([r1, r2, r3, r4]).data)
"""
Fetching PETR4.sa ...
[*********************100%***********************]  1 of 1 completed
Fetching CSNA3.sa ...
[*********************100%***********************]  1 of 1 completed
Fetching USIM5.sa ...
[*********************100%***********************]  1 of 1 completed
        Open    High     Low   Close  Volume
Date                                        
0      99.82  100.73   99.13   99.18   12499
1     101.52  109.90  101.52  109.59   15623
2     109.51  112.20  105.65  111.46   11805
3     111.59  112.56  110.18  110.30   10416
4     110.80  111.08  109.94  110.61   13019
...      ...     ...     ...     ...     ...
147    92.05   93.28   92.05   92.82       5
148    92.34   94.85   92.32   94.16       5
149    93.27   97.09   91.75   93.43       7
150    93.76   97.64   92.09   96.71       7
151    96.71  104.32   96.71  100.05       9

[152 rows x 5 columns]
"""
```

```python3


```


</p>
</details>

**Saving as a CSV file**
<details>
<p>

```python3
from rndqts import Real

Real("VALE3.sa").data.to_csv("/tmp/myfile.csv")


```


</p>
</details>

**Plotting**
<details>
<p>

```python3
from rndqts import Real

Real("VALE3.sa").plot()
"""
Fetching VALE3.sa ...
[*********************100%***********************]  1 of 1 completed
"""

```


</p>
</details>

<p><a href="https://github.com/davips/rndqts/blob/main/examples/plotvale3.png">
<img src="https://raw.githubusercontent.com/davips/rndqts/main/examples/plotvale3.png" alt="Output as a browser window" width="200" height="200">
</a></p>


## Features / TODO

* [x] Fetch from yahoo
* [x] Automatic local caching
* [x] Slicing
* [x] Plot candle sticks
* [x] Realistic random quotes
  * [x] Ticker 'pseudo' generates (not so realistic) data without real quotes dependence (good for tests)

* [x] **Distinct kinds of quotes: Real, Realistic random, Synthetic Random**
  * [x] Cacheable and identified by hash of args
  
  * [x] ***Real*** (market quotes)
  * [x] ***Realistic*** (realistic random quotes, .i.e, it is based on real quotes)
  * [x] ***Synthetic*** (quotes based interily on Gaussian distributions from pseudo random number generator)
    * [x] Lazy/Infinite

* [ ] News fetching
    * [ ] https://blog.datahut.co/scraping-nasdaq-news-using-python
