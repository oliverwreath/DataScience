import pandas as pd 
from ggplot import *

def plot_weather_data(turnstile_weather):
	'''
	data visualization
	focused on the MTA and weather data we used in assignment #3.  
	
	(e.g., scatterplots, line plots, or histograms) or attempt to implement
	something more advanced if you'd like.  

	Here are some suggestions for things to investigate and illustrate:
	 * Ridership by time of day or day of week
	 * How ridership varies based on Subway station
	 * Which stations have more exits or entries at different times of day

	
	'''

	# your code here
	df = turnstile_weather
	# print df.head(10)
	plot = ggplot(df, aes(x ='ENTRIESn_hourly', y='EXITSn_hourly', color='Hour')) + geom_point() + geom_line() + \
		ggtitle("NY Subway In&Out categoried by hour - Oliver")
	return plot
