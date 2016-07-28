import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

magnitudeList = []
errorList = []

dxAverage1 = -3.36777
dyAverage1 = 1.19223

IMAGEOUT = 'LF.png'

matchedStarsFile = open('matchedStarsPartial.out')

print("----------------------------------------")
print("Running Script: Make histogram")

cuts=0
for plotPair in matchedStarsFile:
    xandy = plotPair.split()
    plotX = float(xandy[8])-dyAverage1
    plotY = float(xandy[9])-dxAverage1
    if plotX/.08 > -4:
        cuts+=1
        continue
    
    magnitudeList.append(float(xandy[2]))
    errorList.append(float(xandy[3]))

barBottoms = [0]*37
barTops = [0]*37

(n, bins, patches) = plt.hist(magnitudeList, bins=35, normed=False, color='r', label='disk', log=True, range=[16.5, 25], histtype='step')
plt.xlim([16.5, 25])

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
    
    plt.errorbar(x, y, yerr=yerr, fmt='', ecolor='green', elinewidth=1)

plt.title('Luminosity Function Histogram - F814W')
plt.savefig(IMAGEOUT)
plt.show()