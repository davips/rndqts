# Fetching from Yahoo
from rndqts.quotes import Quotes

print(Quotes("PETR4.sa", progress=False).data)
# ...
