import cPickle as pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from metrics import *

########## PLOT FOR 25% SAND FRACTION SHUFFLE 1 ##########

data = []						# Empty list for mapfile data
fractions = []					# Empty list for fractional metrics
wetlen = []						# Empty list for land area data

T = np.arange(70.0,100.0,1.0)		# Set the x-variable

RUN = 31000000					# Set variable for run number
NUMSTART = 11970				# Set beginning file number
NUMEND = 12000					# Set end file number

for i in range(RUN+NUMSTART, RUN+NUMEND):
	f = open('mapfilestest/shuffled3101/shuffled' + str(i) + '.p', 'r')
	data.append(pickle.load(f))
	f.close()
	
for j in range(0,NUMEND-NUMSTART):
	fractions.append(fractional_areas(data[j]))
	
for k in range(0,NUMEND-NUMSTART):
	wetlen.append(fractions[k]['land'])

fig, ax = plt.subplots()
for i in range(0,NUMEND-NUMSTART):
	ax.plot(T[i], wetlen[i],'k-o')



########## PLOT FOR 25% SAND FRACTION SHUFFLE 2 ##########

data = []						# Empty list for mapfile data
fractions = []					# Empty list for fractional metrics
wetlen = []						# Empty list for land area data

T = np.arange(70.0,100.0,1.0)		# Set the x-variable

RUN = 31000000					# Set variable for run number
NUMSTART = 21970				# Set beginning file number
NUMEND = 22000					# Set end file number

for i in range(RUN+NUMSTART, RUN+NUMEND):
	f = open('mapfilestest/shuffled3102/shuffled' + str(i) + '.p', 'r')
	data.append(pickle.load(f))
	f.close()
	
for j in range(0,NUMEND-NUMSTART):
	fractions.append(fractional_areas(data[j]))
	
for k in range(0,NUMEND-NUMSTART):
	wetlen.append(fractions[k]['land'])

for i in range(0,NUMEND-NUMSTART):
	ax.plot(T[i], wetlen[i],'b-o')



########## PLOT FOR 25% SAND FRACTION SHUFFLE 3 ##########

data = []						# Empty list for mapfile data
fractions = []					# Empty list for fractional metrics
wetlen = []						# Empty list for land data

T = np.arange(70.0,100.0,1.0)		# Set the x-variable

RUN = 31000000					# Set variable for run number
NUMSTART = 31970				# Set beginning file number
NUMEND = 32000					# Set end file number

for i in range(RUN+NUMSTART, RUN+NUMEND):
	f = open('mapfilestest/shuffled3103/shuffled' + str(i) + '.p', 'r')
	data.append(pickle.load(f))
	f.close()
	
for j in range(0,NUMEND-NUMSTART):
	fractions.append(fractional_areas(data[j]))
	
for k in range(0,NUMEND-NUMSTART):
	wetlen.append(fractions[k]['land'])

for i in range(0,NUMEND-NUMSTART):
	ax.plot(T[i], wetlen[i],'g-o')



########## PLOT FOR 25% SAND FRACTION RUN ##########

data = []						# Empty list for mapfile data
fractions = []					# Empty list for fractional metrics
wetlen = []						# Empty list for land area data

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
	wetlen.append(fractions[k]['land'])

for i in range(0,NUMEND-NUMSTART):
	ax.plot(T[i], wetlen[i],'r-o')

ax.set(xlabel = 'Time', ylabel = 'Land Area', title = 'Shuffled Strata Land Area Metrics')
black_patch = mpatches.Patch(color='black', label='25% Shuffled Strata #1')
blue_patch = mpatches.Patch(color='blue', label='25% Shuffled Strata #2')
green_patch = mpatches.Patch(color='green', label='25% Shuffled Strata #3')
red_patch = mpatches.Patch(color='red', label='25% Model Realization')
plt.legend(bbox_to_anchor=(0.,1.02,1.,0.102),loc=3,handles=[black_patch, blue_patch, green_patch, red_patch])
ax.set_xlim(65,105)
#ax.set_ylim(0.0,1.0)

plt.show()
