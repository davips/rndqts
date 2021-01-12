# Fetching from Yahoo
from rndqts.quotes import Quotes

print(Quotes("VALE3.sa").data)
# ...

Quotes("VALE3.sa").plot()
