# finance
Get data from google finance

Steps:
1. Install python 3 from https://www.python.org/downloads/  
2. Goto directory
3. run install.bat
4. Create an empty .xlsx file
5. Update universe: open bin/universe.py example "{'exchange':"NSE",      'name': "RELIANCE" ,      'tab': "RELIANCE"},"
6. For historical data use. 
D:\finance>bin\add_historical_data.py --help
Usage: add_historical_data.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  Read and update file
  -l LOOKBACK, --lookback=LOOKBACK
                        Enter date lookback example 5d, 1Y
Example: bin\add_historical_data.py --file "D:\trade.xlsx" [Default runs for a year]

7. Update periodic data
>bin\update_data.py --help
Usage: update_data.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  Read and update file
  -d DATE, --date=DATE  Enter date in format yyyy-m-d
  -l LOOKBACK, --lookback=LOOKBACK
                        Enter date lookback example 5d, 1Y
  -a ARCHIVE, --archive=ARCHIVE
                        Enter archive location
Example:bin\update_data.py --file "D:\dump.xlsx" --date "2017-7-14"

-- Archived files and logs go to c:\archives\
