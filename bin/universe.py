# Universe
# Add Ticker and and exchange, for now we only have one datasource

class Universe:

	excel_directory = "C:/archives/"

	def __init__(self):
		pass
		
	univ = [
		#{'exchange':"NSE",      'name': "RELIANCE" ,      'tab': "RELIANCE"},
		{'exchange':"NSE",      'name': "INFY",            'tab': "INFY"}
	]

	def universe(self):
		return self.univ
