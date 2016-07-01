import matplotlib.pyplot as plt
import pylab

x = []
y = []
s = 0.25

bulgeFile = open('f2catalog2.csv', 'r')
#diskFile = open('/Users/SeanTerry/Desktop/finalcmd/disk/diskmatlaboutput/plotpointsJ-Hdisk.csv', 'r')

sepFile = bulgeFile.read().split('\r')
## sepDisk = diskFile.read().split('\r')

bulgeFile.close()


for plotPair in sepFile:
	xandy = plotPair.split(',')
	x.append(float(xandy[3]))
	y.append(float(xandy[5]))
	
# for plotPair in sepDisk:
	aandb = plotPair.split(',')
	x.append(float(xandy[3]))
	y.append(float(xandy[5]))
	


plt.scatter(x, y, s)

plt.title('CMD Stanek Field')
plt.xlabel('F110W - F160W')
plt.ylabel('F160W Instrumental Mag')
plt.gca().invert_yaxis()
pylab.xlim([-0.5,3.0])

plt.show()