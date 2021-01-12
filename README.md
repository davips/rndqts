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
2021-01-04   89.349998   91.480003  88.849998   91.459999  37865500
2021-01-05   91.459999   93.000000  90.519997   93.000000  34300300
2021-01-06   94.980003   96.349998  94.400002   96.050003  53722500
2021-01-07   96.610001  102.529999  96.610001  102.320000  74541400
2021-01-08  103.010002  103.349998  98.199997  102.000000  58562700

[5257 rows x 5 columns]

"""
```


</p>
</details>

**Random stock quotes** <details>
<p>

```python3
from rndqts.quotes import Quotes

# Caching real quotes from Yahoo.
Quotes("VALE3.sa").data
Quotes("VALE3.sa").data
Quotes("CSNA3.sa").data
Quotes("USIM5.sa").data

# Generating random quotes.
print(Quotes("rnd", seed=42).data)
"""
Fetching CSNA3.sa ...
[*********************100%***********************]  1 of 1 completed
Fetching USIM5.sa ...
[*********************100%***********************]  1 of 1 completed
Fetching VALE3.sa ...
[*********************100%***********************]  1 of 1 completed
Fetching USIM5.sa ...
[*********************100%***********************]  1 of 1 completed
Fetching CSNA3.sa ...
[*********************100%***********************]  1 of 1 completed
           Open      High       Low     Close    Volume
Date                                                   
0      0.958716  1.012385  0.941743  0.992661         3
1      0.992661  0.991694  0.994605  0.992468         9
2      0.972047  0.972047  1.045165  1.005138        21
3      1.006966  1.016838  0.980640  0.992706        45
4      0.991616  0.980839  1.003747  0.995994        47
...         ...       ...       ...       ...       ...
31419  1.020146  1.014822  1.042014  1.038674  97471132
31420  1.038895  1.033617  1.038895  1.034494  97471134
31421  1.017697  1.029958  1.012547  1.012547  97471136
31422  1.012548  1.000843  1.055767  1.010187  95941276
31423  1.008489  1.018336  0.994228  1.000000  92881556

[31424 rows x 5 columns]

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

## Features / TODO

* [x] Fetch from yahoo
* [x] Automatic local caching
* [x] Slicing
* [x] Plot candle sticks
* [x] Random quotes
       * [x] Ticker 'pseudo' is an option to generate data without real quotes dependence (good for tests)
       * [ ] Explicit real quotes to sample from ('rnd-MSFT,APPL')
       * [ ] 'n' argument fecthes lazily within date interval 
  
