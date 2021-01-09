# rndqts
Random stock market quotes

**Fetching from Yahoo** <details>
<p>

```python3
from rndqts.quotes import Quotes

Quotes("PETR4.sa", progress=False).data
# ```


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
random_quotes = Quotes("rnd", seed=42).data.values
print(random_quotes)
# [[ 1.00947569  1.01632731  1.00068496  1.00548117  0.        ]
 [ 1.03308968  1.02043589  1.05266991  1.03492298  0.        ]
 [ 1.0474458   1.0313998   1.06120381  1.03847023  0.        ]
 ...
 [48.00395581 47.53092332 48.00395581 47.53959697  0.        ]
 [46.76770303 47.33114758 46.53104833 46.53104833  0.        ]
 [47.13603741 47.13603741 45.98647397 46.89410077  0.        ]]
```

```python3


# ```


</p>
</details>
