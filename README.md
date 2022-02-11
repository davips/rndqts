![test](https://github.com/davips/rndqts/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/rndqts/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/rndqts)

# rndqts
Random stock market quotes

<img src="https://raw.githubusercontent.com/davips/rndqts/main/chart.png">

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
                  Open        High        Low       Close    Volume
Date                                                               
2021-01-06   94.980003   96.349998  94.400002   96.050003  53722500
2021-01-07   96.610001  102.529999  96.610001  102.320000  74541400
2021-01-08  103.010002  103.349998  98.199997  101.260002  43879400
2021-01-11  100.250000  101.980003  99.699997  101.980003  29267000
2021-01-12  102.500000  102.620003  99.180000   99.190002  28598500
2021-01-13   98.870003   98.919998  95.739998   96.220001  31658800
2021-01-14   97.220001   98.860001  96.699997   97.800003  20809900
2021-01-15   96.580002   97.199997  93.510002   93.849998  20161700
2021-01-18   93.900002   95.639999  93.550003   94.309998  22667600
2021-01-19    0.000000    0.000000   0.000000   94.059998         0
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
        Open    High     Low   Close  Volume
Date                                        
0       0.00    0.00    0.00   94.29   10000
1      93.16   93.52   88.73   88.73    9644
2      88.28   91.23   88.18   91.23    9870
3      91.40   91.54   86.85   86.85    9542
4      86.10   87.08   83.08   86.46    7633
...      ...     ...     ...     ...     ...
67     93.95   95.23   92.59   93.23     478
68     93.46   99.70   93.46   99.25     330
69     98.13  102.27   96.40  101.02     387
70    102.04  102.60  100.31  100.31     484
71      0.00    0.00    0.00  100.04     484

[72 rows x 5 columns]
"""
```

```python3


```


</p>
</details>

**Synthetic (non-realistic) quotes**
<details>
<p>

```python3
from rndqts import Synthetic

print(Synthetic()[:5].data)
"""
        Open    High     Low   Close  Volume
Date                                        
0     112.22  117.64  104.00  111.43   11868
1     121.24  122.02  100.54  108.78   11689
2     118.44  124.60  110.35  123.54   12208
3     129.35  141.99  127.66  136.83   11958
4     114.05  145.78  102.64  136.04   14673
"""
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


## Features (current or planned)

* [x] Fetch from yahoo
* [x] Automatic local caching
* [x] Slicing
* [x] Plot candle sticks
* [x] Cacheable and identified by hash id

  
* [x] **Distinct kinds of quotes**
  * [x] ***Real*** 
    * market quotes
  * [x] ***Realistic***
    * random, based on real quotes
  * [x] ***Synthetic***
    * entirely based on Gaussian distributions from a pseudo random number generator
    * good for software test
    * lazy / infinite
  * [ ] ***Holding***
    * combination of real quotes, without randomness
    * useful for dataset augmentation with fictional tickers


* [ ] **News fetching**
    * [ ] https://blog.datahut.co/scraping-nasdaq-news-using-python
