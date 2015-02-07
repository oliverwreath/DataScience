import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
					level=logging.INFO, filemode='w')

def reducer():
	'''
	per UNIT along with the total number of ENTRIESn_hourly 
	over the course of May (which is the duration of our data), separated by a tab.
	An example output row from the reducer might look like this: 
	'R001\t500625.0'

	You can assume that the input to the reducer is sorted such that all rows
	corresponding to a particular UNIT are grouped together.
	'''

	counter = {}
	for line in sys.stdin:
		# your code here
		data = line.strip().split("\t")
		if data[0] in counter:
			counter[data[0]] += int(float(data[1]))
		else:
			counter[data[0]] = int(float(data[1]))

	for i in counter: 
		print i, "\t", counter[i]
		
reducer()
