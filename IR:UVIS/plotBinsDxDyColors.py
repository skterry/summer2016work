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

#matlab program - chip1
dxAverage1 = -3.36777
dyAverage1 = 1.19224

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
    color = float(args[4]) - float(args[6])
    mag = float(args[6])
    dx = float(args[8])
    dy = float(args[9])
    

    plotX = dx-dxAverage1
    plotY = dy-dyAverage1
    
    if (plotX/.08)**2 + (plotY/.08)**2 > 64:
        continue
    
    if 0.0<color<0.25 and 18.3<mag<19.0: #disk
        if diskCount>417:
            continue
        dxList.append(dx)
        dyList.append(dy)
        dx1Centroid+=(plotX/.08)
        dy1Centroid+=(plotY/.08)
        diskCount+=1
        colorList.append('red')
        totalMatches+=1
    
    if 0.62<color<0.68 and 18.8<mag<19.2: #bulge
        dxList.append(dx)
        dyList.append(dy)
        dx2Centroid+=(plotX/.08)
        dy2Centroid+=(plotY/.08)
        bulgeCount+=1
        colorList.append('blue')
        totalMatches+=1

disks = 0
bulges = 0

print("\nCalculating separation.............")
numBins = int(totalMatches/BINSIZE)
radius = 1
for i in range(numBins):
    curdx = sum(dxList[i*BINSIZE:(i+1)*BINSIZE])/BINSIZE
    curdy = sum(dyList[i*BINSIZE:(i+1)*BINSIZE])/BINSIZE
    plotX = curdx-dxAverage1
    plotY = curdy-dyAverage1
    
    dxBin.append(plotX/.08)
    dyBin.append(plotY/.08)
    
    if dxBin[i] < -4:
        if colorList[i] == 'red':
            disks+=1
        if colorList[i] == 'blue':
            bulges+=1
            
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