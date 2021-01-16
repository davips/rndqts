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
Fetching VALE3.sa ...
[*********************100%***********************]  1 of 1 completed
                  Open        High        Low       Close    Volume
Date                                                               
2021-01-04   89.349998   91.480003  88.849998   91.459999  37865500
2021-01-05   91.459999   93.000000  90.519997   93.000000  34300300
2021-01-06   94.980003   96.349998  94.400002   96.050003  53722500
2021-01-07   96.610001  102.529999  96.610001  102.320000  74541400
2021-01-08  103.010002  103.349998  98.199997  101.260002  43879400
2021-01-11  100.250000  101.980003  99.699997  101.980003  29267000
2021-01-12  102.500000  102.620003  99.180000   99.190002  28598500
2021-01-13   98.870003   98.919998  95.739998   96.220001  31658800
2021-01-14   97.220001   98.860001  96.699997   97.800003  20809900
2021-01-15   96.580002   97.199997  93.199997   93.550003  31712400
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
0      98.26   99.28   91.50   91.90   12499
1      90.76   93.85   90.24   90.26   13400
2      89.66   94.05   89.36   91.20   16749
3      90.48   93.31   89.88   90.86   13468
4      90.00   95.08   88.92   92.01   15087
...      ...     ...     ...     ...     ...
67    116.65  121.32  115.36  119.70     799
68    119.63  121.19  112.72  116.76     395
69    115.84  116.76  109.17  111.38     307
70    110.73  110.73  104.34  104.55     222
71    103.25  103.91   99.63  100.01     278

[72 rows x 5 columns]
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
