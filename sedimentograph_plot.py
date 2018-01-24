import cPickle as pickle
import numpy as np
import matplotlib.pyplot as plt

fbase = 'data'
froot = 'mapfiles/'

for fnum in range(1070,1100):
	
	fname = froot + fbase + str(fnum) + 'seds' + '.p'
	pickleddata = open(fname,'r')
	data = pickle.load(pickleddata)
	pickleddata.close()
	
	sand_vol = data['sand_vol'][:]
	sand_frac_by_vol = data['sand_frac_by_vol'][:]
	mud_vol = data['mud_vol'][:]
	norm_distance_from_apex = data['norm_distance_from_apex'][:]
	for i in range(0, len(sand_vol)):
		t = norm_distance_from_apex[i]
		plt.scatter(norm_distance_from_apex[i], sand_frac_by_vol[i], c=t, cmap='bone')

plt.xlabel('Normalized distance from delta apex')
plt.ylabel('Subsurface sand fraction by volume')

plt.show()
