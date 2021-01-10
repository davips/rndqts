# Saving as a CSV file
from rndqts.quotes import Quotes

Quotes("PETR4.sa", progress=False).data.to_csv("/tmp/myfile.csv")

