import sys
import matplotlib.pyplot as plt
import numpy as np

dxList = []
dyList = []
dxBin = []
dyBin = []
colorList = []
ALPHA = 1
BINSIZE = 1

IMAGEOUT = 'dxdy.png'

if len(sys.argv)==2:
    IMAGEOUT = sys.argv[1]

matchedStarsFile = open('matchedStars.out')

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

#ird python program - drizzled
#dxAverage = -3.36
#dyAverage = 1.19

#ird python program - from full frame
dxAverage = -3.36688
dyAverage = 1.28508

#dolphot alignment
#dxAverage = -3.36
#dyAverage = 1.19

print("\nBinning.............")
numBins = int(totalMatches/BINSIZE)
for i in range(numBins):
    sys.stdout.write("\r{0}%".format(100*i/numBins+1))
    sys.stdout.flush()
    curdx = sum(dxList[i*BINSIZE:(i+1)*BINSIZE])/BINSIZE
    curdy = sum(dyList[i*BINSIZE:(i+1)*BINSIZE])/BINSIZE
    dxBin.append((curdx-dxAverage)/.04)
    dyBin.append((curdy-dyAverage)/.04)
    #if dxBin[-1] < -7 or dxBin[-1]>7:
    #    dxBin.pop()
    #    dyBin.pop()

if BINSIZE == 1:
    for i in range(numBins):
        if colorList[i] < 2.15:
            colorList[i] = .75
        else:
            colorList[i] = .25
            
print("\n\nCreating plot.............")    
#GENERATE AND DISPLAY SCATTER PLOT
c1 = plt.scatter(dxBin, dyBin, c=colorList, s=30, alpha=ALPHA)
ax = plt.gca() #get current axis
ax.set_ylabel('dy')
ax.set_xlabel('dx')
ax.invert_xaxis()
plt.savefig(IMAGEOUT)
plt.show()