from universe import Universe
from objects.instrument import Instruments
from datasource.google.provider import Provider
import datetime

def main(date):
	univ = Universe()
	provider = Provider()

	"""
	for stock in univ.universe():
	    price = provider.get_last_trade_data(stock['name'], stock['exchange'], "5d")

	    instruments = Instruments(price.to_dict())
	    if(instruments is not None):
	    	print(instruments.get_instrument(date.__str__()))
	"""

	for stock in univ.universe():
		print(stock)
		

main(datetime.date(year=2017, month=7, day=13))