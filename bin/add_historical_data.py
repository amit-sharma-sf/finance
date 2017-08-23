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
	parser.add_option("-l", "--lookback",
                  help="Enter date lookback example 5d, 1Y", default="1Y")
	parser.add_option("-i", "--instrument",
                  help="Enter the instrument ticker")

	return parser.parse_args()

def validate_options(options):
	opts = dict()
	if(options.file is None or not os.path.isfile(options.file)):
		log.critical("Enter Valid Filename")
	else:
		opts['file'] = options.file

	if(options.instrument is None):
		log.critical("Enter Valid Instrument")
	else:
		opts['instrument'] = options.instrument

	opts['lookback'] = options.lookback

	return opts

def main(options):

	parsed_options = validate_options (options)
	log.info("Options: " + str(parsed_options))
	univ = Universe()
	provider = Provider(log)

	for stock in univ.universe():
		if(stock['name'] != parsed_options['instrument']):
			continue

		log.info("Processing: " + stock['name'])
		price = provider.get_last_trade_data(stock['name'], stock['exchange'], parsed_options['lookback'])
		instruments = Instruments(log, price.to_dict())

		if(instruments is not None):
			driver = Driver(log, parsed_options['file'])
			driver.create_tabs(stock['tab'])
			driver.insert_data(instruments.get_instruments(), stock['tab'], 2)
			driver.save()
		
log.basicConfig(filename=Universe().get_archives_location() + 
	'fin_' + str(datetime.date.today()) + '.log', level=log.INFO)
(options, args) = parse_options()
main(options)
