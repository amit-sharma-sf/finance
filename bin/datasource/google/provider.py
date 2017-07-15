import googlefinance.client as gfc

class Provider:
	""" Google Provider for Fin Data"""
	def get_last_trade_data(self, tkr, exchange, duration):
		"""
		tkr should be a valid ticker for the exchange
		echange should be a valid exchange code
		"""
		stock = dict()
		stock['q'] = tkr
		stock['x'] = exchange

		params = list()
		params.append(stock)

		data = gfc.get_prices_data(params, duration)
		return data

