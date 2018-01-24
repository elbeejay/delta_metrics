import cPickle as pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from metrics import *

########## PLOT FOR 25% SAND FRACTION RUN ##########

data = []						# Empty list for mapfile data
fractions = []					# Empty list for fractional metrics
wetlen = []						# Empty list for wetted frac data

T = np.arange(70.0,100.0,1.0)		# Set the x-variable

RUN = 1000						# Set variable for run number
NUMSTART = 70					# Set beginning file number
NUMEND = 100					# Set end file number

for i in range(RUN+NUMSTART, RUN+NUMEND):
	f = open('mapfiles/data' + str(i) + '.p', 'r')
	data.append(pickle.load(f))
	f.close()
	
for j in range(0,NUMEND-NUMSTART):
	fractions.append(fractional_areas(data[j]))
	
for k in range(0,NUMEND-NUMSTART):
	wetlen.append(fractions[k]['frac_wet'])

fig, ax = plt.subplots()
for i in range(0,NUMEND-NUMSTART):
	ax.plot(T[i], wetlen[i],'r-o')



########## PLOT FOR 50% SAND FRACTION RUN ##########

data = []						# Empty list for mapfile data
fractions = []					# Empty list for fractional metrics
wetlen = []						# Empty list for wetted frac data

T = np.arange(70.0,100.0,1.0)		# Set the x-variable

RUN = 2000						# Set variable for run number
NUMSTART = 70					# Set beginning file number
NUMEND = 100					# Set end file number

for i in range(RUN+NUMSTART, RUN+NUMEND):
	f = open('mapfiles/data' + str(i) + '.p', 'r')
	data.append(pickle.load(f))
	f.close()
	
for j in range(0,NUMEND-NUMSTART):
	fractions.append(fractional_areas(data[j]))
	
for k in range(0,NUMEND-NUMSTART):
	wetlen.append(fractions[k]['frac_wet'])

for i in range(0,NUMEND-NUMSTART):
	ax.plot(T[i], wetlen[i],'b-o')



########## PLOT FOR 75% SAND FRACTION RUN ##########

data = []						# Empty list for mapfile data
fractions = []					# Empty list for fractional metrics
wetlen = []						# Empty list for wetted frac data

T = np.arange(70.0,100.0,1.0)		# Set the x-variable

RUN = 3000						# Set variable for run number
NUMSTART = 70					# Set beginning file number
NUMEND = 100					# Set end file number

for i in range(RUN+NUMSTART, RUN+NUMEND):
	f = open('mapfiles/data' + str(i) + '.p', 'r')
	data.append(pickle.load(f))
	f.close()
	
for j in range(0,NUMEND-NUMSTART):
	fractions.append(fractional_areas(data[j]))
	
for k in range(0,NUMEND-NUMSTART):
	wetlen.append(fractions[k]['frac_wet'])

for i in range(0,NUMEND-NUMSTART):
	ax.plot(T[i], wetlen[i],'g-o')

ax.set(xlabel = 'Time', ylabel = 'Wetted Fraction', title = 'Wetted Fraction Metric')
red_patch = mpatches.Patch(color='red', label='25% Sand Fraction')
blue_patch = mpatches.Patch(color='blue', label='50% Sand Fraction')
green_patch = mpatches.Patch(color='green', label='75% Sand Fraction')
plt.legend(bbox_to_anchor=(0.,1.02,1.,0.102),loc=3,handles=[red_patch, blue_patch, green_patch])
ax.set_xlim(65,105)
ax.set_ylim(0.0,1.0)

plt.show()
