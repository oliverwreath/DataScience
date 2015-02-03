import numpy as np

def compute_r_squared(d, p):
	# Write a function that, given two input numpy arrays, 'data', and 'predictions,'
	# returns the coefficient of determination, R^2, for the model that produced 
	# predictions.
	# 
	# Numpy has a couple of functions -- np.mean() and np.sum() --
	# that you might find useful, but you don't have to use them.

	# YOUR CODE GOES HERE
	r_squared = ((d - p)**2).sum()/ ((d - np.mean(d))**2).sum()
	r_squared = 1 - r_squared 

	return r_squared





