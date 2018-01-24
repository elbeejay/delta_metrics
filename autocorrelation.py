import numpy as np

def estimated_autocorrelation(x):
	
	### This method divides through by the variane times n at the end
	## As opposed to dividing by variance times n-k
	
	n = len(x)
	variance = x.var()
	x = x-x.mean()
	r = np.correlate(x,x,mode='full')[-n:]
	result = r/(variance*n)
	return result
