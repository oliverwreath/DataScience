import pandas as pd 
from pandas import *
from ggplot import *

import pandas

def lineplot_compare(hr_by_team_year_sf_la_csv):
	# Write a function, lineplot_compare, that will read a csv file
	# called hr_by_team_year_sf_la.csv and plot it using pandas and ggplot2.
	#
	# This csv file has three columns: yearID, HR, and teamID. The data in the
	# file gives the total number of home runs hit each year by the SF Giants 
	# (teamID == 'SFN') and the LA Dodgers (teamID == "LAN"). Produce a 
	# visualization comparing the total home runs by year of the two teams. 
	# 
	# You can see the data in hr_by_team_year_sf_la_csv
	# at the link below:
	# https://www.dropbox.com/s/wn43cngo2wdle2b/hr_by_team_year_sf_la.csv
	#
	# Note that to differentiate between multiple categories on the 
	# same plot in ggplot, we can pass color in with the other arguments
	# to aes, rather than in our geometry functions. For example, 
	# ggplot(data, aes(xvar, yvar, color=category_var)). This should help you 
	# in this exercise.
	
	#YOUR CODE GOES HERE
	df = pd.read_csv(hr_by_team_year_sf_la_csv)
	# df1 = df[df['teamID'] == 'LAN']
	# df2 = df[df['teamID'] == 'SFN']
	# print df.head(10)
	gg = ggplot(df, aes(x='yearID', y='HR', color='teamID')) + geom_point() + geom_line() + \
	ggtitle("Homeruns Comparison - SF Giants v.s. LA Dodgers by Oliver") + xlab("Year") + ylab("Homeruns")
	# ggplot(df, aes(df2['yearID'], df2['HR'], color=df['teamID']))
	# gg = 
	return gg
