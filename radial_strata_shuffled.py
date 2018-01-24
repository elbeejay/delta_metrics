import numpy as np
import matplotlib.pyplot as plt
from file_util import load_matlab_data
import scipy.io

# Load and plot radial stratigraphy from the 70th and 100th (final) time step

# Set radius
r0 = 25.0

bdata = scipy.io.loadmat('25sand/100m/shuffled3101.mat') # Pick file to use
bstrata = bdata['synthetic'] 	# Loading 3D strata array

bzmaxn = np.shape(bstrata)[2]	# Integer equal to depth of strata array
bcircslice = np.zeros((int(np.round(np.pi*r0)*2), int(bzmaxn+1)))	# Zeros 2D array 1st dim is integer of circumference, 2nd dim is max depth + 1
	
bxoir = 5	# This is an integer representing the x origin coordinate
byori = np.shape(bstrata)[1]/2	# This is an integer half the size of the 2nd strata dimension
bcnmax = np.shape(bcircslice)[0]	# This is an integer equal to the computed circumference value
coord = np.zeros((bcnmax,2))	# Zero array to hold coordinates

for bcn in range(0,bcnmax):	# Looping from 0 to the circumference value
	div = float(bcn)/float(bcnmax)	# Float division
	btht = div*np.pi-np.pi/2	# Loop value divided by the circumference times pi minus pi divided by 2 -- gives you theta values between -pi/2 and pi/2
	bic = bxoir + np.cos(btht)*r0	# equal to x integer times cosine of the theta times radius
	bjc = byori + np.sin(btht)*r0	# equal to y integer times sine of the theta times radius
	bbin = int(np.round(bic))		# rounded bic
	bbjn = int(np.round(bjc))		# rounded bjc
	coord[bcn,:] = [bbin, bbjn]		# array holding coordinates of arc
	for z in range(0,bzmaxn):	# Looping from 0 to max depth
		bcircslice[bcn,z] = bstrata[bbin, bbjn, z]	# Set value of slice at bcn number and depth to be equal to strata value at coordinate bbin, bbjn, depth

bcircslice[:,0] = -1		# Define wet area in beginning
bcircslice = np.fliplr(bcircslice)	# flip matrix left right for some reason

plt.subplot(2,1,1)								# Plotting the x-y plane with slice in red
plt.imshow(bstrata[:,:,bzmaxn/2],cmap='bone')
for i in range(0,np.shape(coord)[0]):
	x = int(coord[i,0])
	y = int(coord[i,1])
	plt.scatter(y,x,s=3,c='red')

plt.subplot(2,1,2)								# Plotting the vertical slice
plt.imshow(np.transpose(bcircslice), extent=[0,200,0,100], cmap = 'bone')

plt.show()			# Display plots

## 100th time step
#edata = load_matlab_data('ForHollyMichael/','data1100')
#estrata = edata['strata']

#ezmaxn = np.shape(estrata[2])[1]
#ecircslice = np.zeros(np.round(np.pi)*2, ezmaxn+1)
