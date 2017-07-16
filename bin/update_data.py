from universe import Universe
from objects.instrument import Instruments
from datasource.google.provider import Provider
from driver.excel.excel_driver import Driver
from optparse import OptionParser
from shutil import copyfile

import os.path
import datetime
import logging as log

def parse_options():
	parser = OptionParser()
	parser.add_option("-f", "--file",
                  help="Read and update file")
	parser.add_option("-d", "--date",
                  help="Enter date in format yyyy-m-d")
	parser.add_option("-l", "--lookback",
                  help="Enter date lookback example 5d, 1Y", default="2d")
	parser.add_option("-a", "--archive",
                  help="Enter archive location", default=Universe().get_archives_location())

	return parser.parse_args()

def validate_options(options):
	opts = dict()
	if(options.file is None or not os.path.isfile(options.file)):
		log.critical("Enter Valid Filename")
	else:
		opts['file'] = options.file

	if(options.date is None):
		log.critical("Enter valid Date")
	else:
		(year,month,day) = options.date.split("-")
		date = datetime.date(int(year),int(month),int(day))
		if(date is None):
			log.critical("Enter valid date: " + options.date)
		opts['date'] = str(date)

	if(not os.path.isdir(options.archive)):
		log.critical("Enter valid archive location")
	else:
		opts['archive'] = options.archive

	opts['lookback'] = options.lookback

	return opts

def main(options):

	parsed_options = validate_options (options)
	log.info("Options: " + str(parsed_options))
	univ = Universe()
	provider = Provider(log)
	backup_name = parsed_options['archive'] + str(datetime.date.today()) + os.path.basename(parsed_options['file'])
	log.info("Backing up the file: " + parsed_options['file'] + " to " + backup_name)
	copyfile(parsed_options['file'], backup_name)

	for stock in univ.universe():
		price = provider.get_last_trade_data(stock['name'], stock['exchange'], parsed_options['lookback'])
		instruments = Instruments(log, price.to_dict())
		instrument =  None

		if(instruments is not None):
			instrument = instruments.get_instrument(parsed_options['date'])

		if(instrument is not None):
			driver = Driver(log, parsed_options['file'])
			driver.append_data([instrument], stock['tab'])
			driver.save()
		
log.basicConfig(filename=Universe().get_archives_location() + 
	'fin_' + str(datetime.date.today()) + '.log', level=log.INFO)

(options, args) = parse_options()
main(options)
