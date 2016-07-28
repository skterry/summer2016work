import matplotlib.pyplot as plt
import pylab

x = []
y = []
s = 2

#matlab program - chip1
dxAverage1 = -3.278
dyAverage1 = 1.283

#matlab program - chip2
dxAverage2 = -3.192
dyAverage2 = 1.384

sepFile = open('matchedStarsMerged.out')#bulgeFile.read().split('\r')
## sepDisk = diskFile.read().split('\r')

#bulgeFile.close()

i=0
cuts=0
for plotPair in sepFile:
	xandy = plotPair.split()
    	curdx = float(xandy[2])
    	curdy = float(xandy[3])
	
        if (i < (15585)):
            plotX = curdx-dxAverage2
            plotY = curdy-dyAverage2
            if plotX/.08 > -2.5 or plotY/.08>-2.5:
                cuts+=1
                #continue
        else:
            plotX = curdx-dxAverage1
            plotY = curdy-dyAverage1
            if plotX/.08 > -2.5 or plotY/.08>-2.5:
                cuts+=1
                #continue
    
	x.append(float(xandy[4]))
	y.append(float(xandy[5]))
	i+=1

print("Cuts",cuts)    
plt.scatter(x, y, s=s, alpha = 0.5, marker=".")
plt.title('CMD Stanek Field')
plt.xlabel('F555W - F814W')
plt.ylabel('F814W Instrumental Mag')
plt.gca().invert_yaxis()
pylab.xlim([1.0,5.0])
pylab.ylim([24,15])

x = []
y = []
s = 2

plt.show()

sepFile = open('propVals.txt')
for plotPair in sepFile:
        if '#' in plotPair:
                continue
	line = filter(None,plotPair.split(' '))
        mag555 = float(line[27])
        mag814 = float(line[43])
	x.append(mag555-mag814+1.3)
	y.append(mag814+15.5)
	
plt.scatter(x, y, s=s, alpha = 0.5, marker=".", color='r')

plt.show()