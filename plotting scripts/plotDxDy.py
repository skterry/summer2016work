import sys
import matplotlib.pyplot as plt
import numpy as np

dxList = []
dyList = []
dxBin = []
dyBin = []
colorList = []
ALPHA = .5
BINSIZE = 1

IMAGEOUT = 'dxdy.png'

#number of chip 2 rows = 40274

if len(sys.argv)==2:
    IMAGEOUT = sys.argv[1]

matchedStarsFile = open('matchedStarsBranches.out')

print("----------------------------------------")
print("Running Script: Average, bin, and plot")

print("\nLoading dx and dy.............")
totalMatches = 0
for line in matchedStarsFile:
    args = line.split()
    dxList.append(float(args[2]))
    dyList.append(float(args[3]))
    colorList.append(float(args[4]))
    totalMatches+=1

#matlab program - chip1
dxAverage1 = -3.278
dyAverage1 = 1.283

#matlab program - chip2
dxAverage2 = -3.192
dyAverage2 = 1.384

#ird program - chip 1
#dxAverage1 = -3.37293888426
#dyAverage1 = 1.28905678601

#ird program - chip 2
#ird program - chip 2
#dxAverage2 = -3.07407676245
#dyAverage2 = 1.35405712439


print("\nBinning.............")
numBins = int(totalMatches/BINSIZE)
radius = 1
for i in range(numBins):
    sys.stdout.write("\r{0}%".format(100*i/numBins+1))
    sys.stdout.flush()
    curdx = sum(dxList[i*BINSIZE:(i+1)*BINSIZE])/BINSIZE
    curdy = sum(dyList[i*BINSIZE:(i+1)*BINSIZE])/BINSIZE
    if (i < 460/BINSIZE):
        plotX = curdx-dxAverage2
        plotY = curdy-dyAverage2
        if plotX**2+plotY**2<radius:
            dxBin.append(plotX/.04)
            dyBin.append(plotY/.04)
        else:
            colorList.pop(i)
    else:
        plotX = curdx-dxAverage1
        plotY = curdy-dyAverage1
        if plotX**2+plotY**2<radius:
            dxBin.append(plotX/.04)
            dyBin.append(plotY/.04)
        else:
            colorList.pop(i)
    #if dxBin[-1] < -7 or dxBin[-1]>7:
    #    dxBin.pop()
    #    dyBin.pop()
dx1Centroid = 0.0
dy1Centroid = 0.0
dx2Centroid = 0.0
dy2Centroid = 0.0

diskCount = 0 #left side - dx1/dy1
bulgeCount = 0 #right side - dx2/dy2

numBins = int(len(dxBin))

if BINSIZE == 1:
    for i in range(numBins):
        if colorList[i] < 2.05:
            dx1Centroid+=dxBin[i]
            dy1Centroid+=dyBin[i]
            diskCount+=1
            colorList[i] = .75#blue
        else:
            dx2Centroid+=dxBin[i]
            dy2Centroid+=dyBin[i]
            bulgeCount+=1
            colorList[i] = .25#red
    dx1Centroid = dx1Centroid /diskCount
    dy1Centroid = dy1Centroid /diskCount
    dx2Centroid = dx2Centroid /bulgeCount
    dy2Centroid = dy2Centroid /bulgeCount
    
    print("\nCentroid values......")
    print(dx1Centroid)
    print(dy1Centroid)
    print(dx2Centroid)
    print(dy2Centroid)
    
       
print("\n\nCreating plot.............")    
#GENERATE AND DISPLAY SCATTER PLOT
if BINSIZE == 1:
    c1 = plt.scatter(dxBin, dyBin,c=colorList, s=30, alpha=ALPHA)
else:
    c1 = plt.scatter(dxBin, dyBin, s=30, alpha=ALPHA)
ax = plt.gca() #get current axis
ax.set_ylabel(r'$\mu_b $, mas/yr')
ax.set_xlabel(r'$\mu_l $, mas/yr')

#ADD LINES
ax.axhline(dy1Centroid, linestyle='-', color='b') # horizontal lines disk
ax.axvline(dx1Centroid, linestyle='-', color='b') # vertical lines disk

ax.axhline(dy2Centroid, linestyle='-', color='r') # horizontal lines bulge
ax.axvline(dx2Centroid, linestyle='-', color='r') # vertical lines bulge

ax.invert_xaxis()
plt.title('Vector Point Diagram')
plt.savefig(IMAGEOUT)
plt.show()