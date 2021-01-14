![test](https://github.com/davips/rndqts/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/rndqts/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/rndqts)

# rndqts
Random stock market quotes

[Latest version](https://github.com/davips/rndqts)

## Installation
### as a standalone lib.
```bash
# Set up a virtualenv. 
python3 -m venv venv
source venv/bin/activate

# Install from PyPI...
pip install rndqts

# ...or, install from updated source code.
pip install git+https://github.com/davips/rndqts
```

### as an editable lib inside your project.
```bash
cd your-project
source venv/bin/activate
git clone https://github.com/davips/rndqts ../rndqts
pip install -e ../rndqts
```

## Examples

<<real>>

<<rnd>>

<<ascsv>>

<<plot>>

<p><a href="https://github.com/davips/rndqts/blob/main/examples/plotvale3.png">
<img src="examples/plotvale3.png" alt="Output as a browser window" width="200" height="200">
</a></p>


## Features / TODO

* [x] Fetch from yahoo
* [x] Automatic local caching
* [x] Slicing
* [x] Plot candle sticks
* [x] Realistic random quotes
  * [x] Ticker 'pseudo' generates (not so realistic) data without real quotes dependence (good for tests)

* [ ] **Separate classes: Real, Random, Pseudo**
  * [ ] Cacheable and identified by hash of args
  
  * [ ] ***Real*** (market quotes)
    * [ ] Args: ticker, start/end dates, slice<sup>1</sup>
      * [ ] Default dates interval: 2020-01-01 - 2020-12-31
  
  * [ ] ***Random*** (realistic random quotes, .i.e, it is based on real quotes)
    * [ ] Args: rndqts objects, seed, slice<sup>1</sup>


  * [ ] ***Pseudo*** (pseudo random quotes)
    * [ ] Args: seed, slice<sup>1</sup>
    * [ ] Lazy

* [ ] News fetching
    * [ ] https://blog.datahut.co/scraping-nasdaq-news-using-python
    
<sup>1</sup>Slicing is intended to be done via squared brackets syntax, e.g., `quotes[3:40]`, not directly.
