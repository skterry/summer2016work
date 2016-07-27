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

matchedStarsFile = open('matchedStarsFull.out')

print("----------------------------------------")
print("Running Script: Average, bin, and plot")

print("\nLoading dx and dy.............")

dx1Centroid = 0.0
dy1Centroid = 0.0
dx2Centroid = 0.0
dy2Centroid = 0.0

diskCount = 0 #left side - dx1/dy1
bulgeCount = 0 #right side - dx2/dy2

totalMatches = 0
for i, line in enumerate(matchedStarsFile):
    args = line.split()
    color = float(args[2]) - float(args[4])
    mag = float(args[4])
    dx = float(args[5])
    dy = float(args[6])
    if 0.0<color<.6 and 18<mag<18.8: #disk
        #if diskCount>122:
        #    continue
        dxList.append(dx)
        dyList.append(dy)
        dx1Centroid+=dx
        dy1Centroid+=dy
        diskCount+=1
        colorList.append('red')
        totalMatches+=1
    
    if 1.46<color<1.65 and 17.5<mag<18.5: #bulge
        dxList.append(dx)
        dyList.append(dy)
        dx2Centroid+=dx
        dy2Centroid+=dy
        bulgeCount+=1
        colorList.append('blue')
        totalMatches+=1

dx1Centroid = dx1Centroid /diskCount
dy1Centroid = dy1Centroid /diskCount
dx2Centroid = dx2Centroid /bulgeCount
dy2Centroid = dy2Centroid /bulgeCount

print(diskCount)
print(bulgeCount)

print("\nCentroid values......")
print(dx1Centroid)
print(dy1Centroid)
print(dx2Centroid)
print(dy2Centroid)

#matlab program - chip1
dxAverage1 = -3.36777
dyAverage1 = 1.19224

disks = 0
bulges = 0

print("\nBinning.............")
numBins = int(totalMatches/BINSIZE)
radius = 1
for i in range(numBins):
    curdx = sum(dxList[i*BINSIZE:(i+1)*BINSIZE])/BINSIZE
    curdy = sum(dyList[i*BINSIZE:(i+1)*BINSIZE])/BINSIZE
    plotX = curdx-dxAverage1
    plotY = curdy-dyAverage1
    dxBin.append(plotX/.08)
    dyBin.append(plotY/.08)
    
    if dxBin[i] < -4.5:
        if colorList[i] == 'red':
            disks+=1
        if colorList[i] == 'blue':
            bulges+=1
print("\n\nDisks, bulges.............")    
print(str(disks) + " " + str(bulges))    
 
print("\n\nCreating plot.............")    
#GENERATE AND DISPLAY SCATTER PLOT
plt.scatter(dxBin, dyBin,c=colorList, s=30, alpha=ALPHA)

ax = plt.gca() #get current axis
ax.set_ylabel('dy')
ax.set_xlabel('dx')

#ADD LINES
ax.axhline(dy1Centroid, linestyle='-', color='b') # horizontal lines disk
ax.axvline(dx1Centroid, linestyle='-', color='b') # vertical lines disk

ax.axhline(dy2Centroid, linestyle='-', color='r') # horizontal lines bulge
ax.axvline(dx2Centroid, linestyle='-', color='r') # vertical lines bulge

ax.invert_xaxis()
plt.savefig(IMAGEOUT)
plt.show()