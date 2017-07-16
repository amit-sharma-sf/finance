# Universe
# Add Ticker and and exchange, for now we only have one datasource

class Universe:

	# If changing this, please make sure to update the install.bat file
	archives_directory = "C:/archives/"
	logger = None
	def __init__(self):
		pass
	
	# Add the instruments here	
	univ = [
		{'exchange':"NSE",      'name': "RELIANCE" ,      'tab': "RELIANCE"},
		{'exchange':"NSE",      'name': "INFY",           'tab': "INFY"}
	]
	###############################3
	def universe(self):
		return self.univ

	def get_archives_location(self):
		return self.archives_directory
