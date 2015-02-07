import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
					level=logging.INFO, filemode='w')

def mapper():
	"""
	In this exercise, for each turnstile unit, you will determine the date and time 
	(in the span of this data set) at which the most people entered through the unit.
	
	The input to the mapper will be the final Subway-MTA dataset, the same as
	in the previous exercise. You can check out the csv and its structure below:
	https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

	For each line, the mapper should return the 
	UNIT, ENTRIESn_hourly, DATEn, and TIMEn columns, separated by tabs. For example:
	1, 6, 2, 3
	'R001\t100000.0\t2011-05-01\t01:00:00'

	Since you are printing the output of your program, printing a debug 
	statement will interfere with the operation of the grader. Instead, 
	use the logging module, which we've configured to log to a file printed 
	when you click "Test Run". For example:
	logging.info("My debugging message")
	"""

	sys.stdin.next()
	for line in sys.stdin:
		# your code here
		data = line.strip().split(",")
		print data[1], "\t", data[6], "\t", data[2], "\t", data[3]

mapper()
