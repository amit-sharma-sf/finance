import datetime

class Instruments:
	instruments = list()
	# Constants
	OPEN  = "Open"
	CLOSE = "Close"
	HIGH  = "High"
	LOW   = "Low"
	NAME  = "Name"
	DATE  = "Date"

	def __init__(self, data):
		keys = list(data.keys())
		if(keys.__len__() < 4):
			print("Error creating instrument: " + data)
		#date = list(data[keys[0]].keys())[0]
		name = keys[0].split("_")[0]

		for date in list(data[keys[0]].keys()):
			inst  = dict()
			inst[self.DATE] = date.__str__()
			inst[self.NAME] = name
			inst[self.OPEN]  = data[name + "_" + self.OPEN][date]
			inst[self.CLOSE] = data[name + "_" + self.CLOSE][date]
			inst[self.HIGH]  = data[name + "_" + self.HIGH][date]
			inst[self.LOW]   = data[name + "_" + self.LOW][date]

			self.instruments.append(inst)

	def get_instruments(self):
		return self.instruments

	def get_instrument(self, date):
		print (date)
		for inst in self.instruments:
			if(inst[self.DATE] == date):
				return inst

		return None