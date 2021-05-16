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
Fetching VALE3.SA ...
[*********************100%***********************]  1 of 1 completed
                 Open       High        Low      Close    Volume
Date                                                            
2020-12-17  82.771173  84.158663  82.455396  83.440994  21367800
2020-12-18  83.842888  84.570121  83.661076  84.015129  23843100
2020-12-21  82.436261  83.632377  81.125317  83.115654  31877300
2020-12-22  83.115654  83.240048  81.747298  83.192207  23157000
2020-12-23  82.799879  83.756771  82.675485  83.594101  17710200
2020-12-28  84.005561  84.761506  83.326168  83.546249  26001300
2020-12-29  84.177801  84.397882  82.780740  83.316597  19727500
2020-12-30  83.431427  83.814178  82.914705  83.680214  30102700
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
Fetching PETR4.SA ...
[*********************100%***********************]  1 of 1 completed
Fetching CSNA3.SA ...
[*********************100%***********************]  1 of 1 completed
Fetching USIM5.SA ...
[*********************100%***********************]  1 of 1 completed
        Open    High     Low   Close  Volume
Date                                        
0      99.71  105.87   99.28  104.65   12499
1     105.44  105.72  103.69  104.36    9484
2     103.58  105.33  103.31  104.65   11855
3     104.25  104.72   99.10   99.80    5155
4      98.36   98.99   97.81   98.99    6444
5      99.65  100.64   99.10   99.94    2998
6     100.43  101.34   99.62   99.88    3748
7      97.59  100.78   93.42   98.84    2410
8      99.58  100.67   96.47   97.76    1495
9      97.76   97.91   96.15   97.85    1087
10     99.29   99.85   98.66   98.66     805
11     98.12   98.41   95.27   96.29     764
12     96.75   97.59   96.54   96.95     853
13     98.14   98.21   93.27   95.50     851
14     95.05   96.15   94.91   95.96     651
15     94.51   94.58   89.68   91.43     444
16     91.43   92.96   91.29   91.35     555
17     91.81   92.07   91.09   91.81     488
18     93.59   95.77   92.71   94.87     510
19     94.72   97.32   94.43   96.96     630
20     96.50   96.70   95.67   96.30     565
21     98.56  102.95   95.44   97.31     707
22     98.35   99.30   96.96   97.88     390
23     98.16   98.59   92.45   93.53     239
24     93.66   94.09   93.08   93.94     299
25     92.80   97.65   92.73   95.36     300
26     96.04   96.21   94.72   95.66     247
27     93.86   95.22   92.37   94.64     309
28     94.12   94.85   91.24   92.95     229
29     92.38   93.21   88.42   89.13     169
30     89.27   89.54   86.88   87.21     137
31     87.38   87.61   83.80   84.49     150
32     87.32   89.52   86.36   87.87      68
33     87.62   88.09   87.19   87.65      55
34     86.72   87.96   85.90   87.14      69
35     86.94   89.12   86.42   88.72      60
36     88.60   89.15   88.19   88.33      40
37     88.15   91.93   87.92   91.17      37
38     91.60   91.74   90.56   90.73      47
39     87.79   88.76   85.63   87.24      59
40     86.63   87.83   86.47   86.96      72
41     88.29   93.05   88.23   91.27      90
42     91.48   92.03   89.24   89.64     104
43     89.89   90.34   89.42   89.86     129
44     90.36   93.21   89.66   91.49     162
45     93.24   94.75   91.91   92.48     122
46     90.72   91.58   88.65   89.50     117
47     89.85   94.52   89.44   93.85     147
48     93.23   93.75   92.31   92.96     184
49     92.50   93.26   91.68   93.01     126
50     92.36   95.63   91.72   94.81     158
51     95.33   98.18   95.05   97.14     167
52     96.66   97.42   96.38   96.66     190
53     95.94   99.03   94.91   97.73     238
54     98.34  102.73   97.46  101.92     298
55    102.64  103.35   99.13   99.99     143
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

print((Real("VALE3.sa").data))
# Real("VALE3.sa").plot()
"""
Fetching VALE3.sa ...
[*********************100%***********************]  1 of 1 completed
"""

"""
                 Open       High        Low      Close    Volume
Date                                                            
2020-12-17  82.771173  84.158663  82.455396  83.440994  21367800
2020-12-18  83.842888  84.570121  83.661076  84.015129  23843100
2020-12-21  82.436261  83.632377  81.125317  83.115654  31877300
2020-12-22  83.115654  83.240048  81.747298  83.192207  23157000
2020-12-23  82.799879  83.756771  82.675485  83.594101  17710200
2020-12-28  84.005561  84.761506  83.326168  83.546249  26001300
2020-12-29  84.177801  84.397882  82.780740  83.316597  19727500
2020-12-30  83.431427  83.814178  82.914705  83.680214  30102700
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
