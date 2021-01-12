# Saving as a CSV file
from rndqts.quotes import Quotes

Quotes("VALE3.sa").data.to_csv("/tmp/myfile.csv")

