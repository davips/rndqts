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

<<real>>

<<rnd>>

<<ascsv>>

<<plot>>

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
