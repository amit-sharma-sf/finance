import datetime

class Instruments:
	instruments = list()
	logger = None
	# Constants
	OPEN  = "Open"
	CLOSE = "Close"
	HIGH  = "High"
	LOW   = "Low"
	NAME  = "Name"
	DATE  = "Date"

	def __init__(self, log, data):
		self.logger = log

		keys = list(data.keys())
		if(keys.__len__() < 4):
			self.logger.error("Error creating instrument: " + data)

		name = keys[0].split("_")[0]

		for date in list(data[keys[0]].keys()):
			inst  = dict()
			inst[self.DATE] = date.__str__()
			inst[self.NAME] = name
			inst[self.OPEN]  = data[name + "_" + self.OPEN][date]
			inst[self.CLOSE] = data[name + "_" + self.CLOSE][date]
			inst[self.HIGH]  = data[name + "_" + self.HIGH][date]
			inst[self.LOW]   = data[name + "_" + self.LOW][date]

			self.logger.debug("Instrument Added " + inst.__str__())
			self.instruments.append(inst)

	def get_instruments(self):
		return self.instruments

	def get_instrument(self, date):
		for inst in self.instruments:
			if(inst[self.DATE] == date):
				self.logger.info("Found instrument: " + inst.__str__())
				return inst

		return None