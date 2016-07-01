import matplotlib.pyplot as plt
import pylab

x = []
y = []
s = 0.25

#bulgeFile = open('f2catalog2.csv', 'r')
#diskFile = open('/Users/SeanTerry/Desktop/finalcmd/disk/diskmatlaboutput/plotpointsJ-Hdisk.csv', 'r')

sepFile = open('F555_814.out')#bulgeFile.read().split('\r')
## sepDisk = diskFile.read().split('\r')

#bulgeFile.close()


for plotPair in sepFile:
	xandy = plotPair.split(' ')
	x.append(float(xandy[7]))
	y.append(float(xandy[5]))
	
# for plotPair in sepDisk:
	aandb = plotPair.split(' ')
	x.append(float(xandy[7]))
	y.append(float(xandy[5]))
	


plt.scatter(x, y, s=s, alpha = 0)

plt.title('CMD Stanek Field')
plt.xlabel('F555W - F814W')
plt.ylabel('F160W Instrumental Mag')
plt.gca().invert_yaxis()
pylab.xlim([-0.5,5.0])

plt.show()