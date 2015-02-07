import sys
import string
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
					level=logging.INFO, filemode='w')

def reducer():
	#Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

	#Each line will be a key-value pair separated by a tab character.
	#Print out each key once, along with the total number of Aadhaar 
	#generated, separated by a tab. Make sure each key-value pair is 
	#formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

	#Since you are printing the output of your program, printing a debug 
	#statement will interfere with the operation of the grader. Instead, 
	#use the logging module, which we've configured to log to a file printed 
	#when you click "Test Run". For example:
	#logging.info("My debugging message")

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
