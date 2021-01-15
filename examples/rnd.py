# Random stock quotes
from rndqts import Realistic
from rndqts import Real

# Real quotes to fetch from Yahoo.
r1 = Real("PETR4.sa")
r2 = Real("CSNA3.sa")
r3 = Real("VALE3.sa")
r4 = Real("USIM5.sa")

# Generating random quotes.
print(Realistic([r1, r2, r3, r4]).data)
# ...

