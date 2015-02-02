
import math

def t(s1, s2, n1, n2, u1, u2):
	print ( (u1-u2)/ math.sqrt(s1/n1 + s2/n2) )

def v(s1, s2, n1, n2):
	print (((s1/n1 + s2/n2)**2) / (s1**2/n1/n1/(n1-1)+ s2**2/n2/n2/(n2-1)))

print "t="
t(.05, .08, 150, 165, .299, .307)
print "v="
v(.05, .08, 150, 165)


import scipy.stats 

scipy.stats.ttest_ind(list_1, list_2, equal_var=False) 


