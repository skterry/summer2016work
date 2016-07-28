import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

magnitudeList = []
errorList = []

magnitudeListRejected = []
errorListRejected = []

dxAverage1 = -3.36777
dyAverage1 = 1.19223

IMAGEOUT = 'LF.png'

matchedStarsFile = open('matchedStarsFull.out')

print("----------------------------------------")
print("Running Script: Make histogram")

cuts=0
for plotPair in matchedStarsFile:
    xandy = plotPair.split()
    plotX = float(xandy[8])-dxAverage1
    plotY = float(xandy[9])-dyAverage1
    if plotX/.08 > -5:
        cuts+=1
        magnitudeListRejected.append(float(xandy[2]))
        errorListRejected.append(float(xandy[3]))
        continue
    
    magnitudeList.append(float(xandy[2]))
    errorList.append(float(xandy[3]))
barBottoms = [0]*37
barTops = [0]*37

(n, bins, patches) = plt.hist(magnitudeList, bins=25, normed=False, color='r', label='disk', log=True, range=[17, 26.5], histtype='step')
plt.xlim([17, 26.5])
print(len(magnitudeList))
#(n, bins, patches) = plt.hist(magnitudeListRejected, bins=25, normed=False, color='b', label='disk', log=True, range=[16.5, 27], histtype='step')

for magIndex, mag in enumerate(magnitudeList):
    error = errorList[magIndex]
    for edgeIndex, edge in enumerate(bins):
        if abs(mag-edge)<error: #check if the specific star is within the edge of the bin
            barBottoms[edgeIndex]+=1 #current bin can go down
            if mag-edge > 0: #magnitude is on right side of edge
                barTops[edgeIndex-1]+=1
            else: #magnitude is on left side of edge
                barTops[edgeIndex+1]+=1

bin_centres = (bins[:-1] + bins[1:])/2.

for index, height in enumerate(n):
    x = bin_centres[index]
    y = height + (barTops[index] - barBottoms[index])/2
    yerr = (barTops[index] + barBottoms[index])/2
    
    #plt.errorbar(x, y, yerr=yerr, fmt='', ecolor='green', elinewidth=1)

plt.title('Luminosity Function Histogram')
plt.savefig(IMAGEOUT)
plt.show()