import numpy as np
import pandas

def compute_cost(features, values, theta): 
	"""
	Compute the cost of a list of parameters, theta, given a list of features 
	(input data points) and values (output data points).
	"""
	m = len(values)
	sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
	cost = sum_of_square_errors / (2*m)

	return cost

def gradient_descent(features, values, theta, alpha, num_iterations): 
	"""
	Perform gradient descent given a data set with an arbitrary number of features.
	"""

	# Write code here that performs num_iterations updates to the elements of theta.
	# times. Every time you compute the cost for a given list of thetas, append it 
	# to cost_history.
	# See the Instructor notes for hints. 
	
	cost_history = [] 
	# print features.shape
	# print features.shape[0] #1157
	# print features.shape[1] #3
	m = features.shape[0]
	# print "features=", features
	# print "values=", values
	# print "theta=", theta
	# print "alpha=", alpha
	# print "num_iterations=", num_iterations

	###########################
	### YOUR CODE GOES HERE ###
	###########################
	# print features.shape
	# print len(theta)
	# print range(1, features.shape[1])
	for k in range(num_iterations): 
		cost_history.append(compute_cost(features, values, theta))
		# print "latest_cost=", latest_cost
		# print "np.unique(np.dot(features, theta))=", np.unique(np.dot(features, theta)) 
		# print "np.dot(features, theta)=", np.dot(features, theta)
		# print "values - np.dot(features, theta)=", values - np.dot(features, theta)
		# print "theta=", theta
		errors = np.dot(features, theta)
		theta = theta + alpha/m * np.dot((values - errors), features)

	return theta, pandas.Series(cost_history) # leave this line for the grader



