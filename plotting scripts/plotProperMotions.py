#SCRIPT TO VIEW MOTIONS OF FIRST 16 STARS

import sys
import matplotlib.pyplot as plt

ALPHA = 1
DXJITTER = -3.36688
DYJITTER = 1.28508

maxXRange = 0
maxYRange = 0
dxPlot = []
dyPlot = []
star1Pos = []
star2Pos = []
starList2010 = []
starList2012 = []

if len(sys.argv)==2:
    IMAGEOUT = sys.argv[1]

matchedStarsFile = open('matchedStars.out')
starFile2010 = open('2010chip1cols.out')
starFile2012 = open('2012chip1cols.out')

print("----------------------------------------")
print("Running Script: Plot 16 proper motions")

totalMatches = 0
for line in matchedStarsFile:
    args = line.split()
    dx = float(args[2])-DXJITTER
    dy = float(args[3])-DYJITTER
    
    dxPlot.append([-dx/2, dx/2])
    dyPlot.append([-dy/2, dy/2])
    
    if dx/2 > maxXRange:
        maxXRange = dx/2
    if dy/2 > maxYRange:
        maxYRange = dy/2
    
    totalMatches+=1
    if totalMatches > 15:
        break
        
#WIDEN FRAME PARAMETER        
maxXRange = maxXRange*1.15 
maxYRange = maxYRange*1.15
   
myList = ['a' for i in range(16)]
print("\n\nCreating plot.............")    
#GENERATE AND DISPLAY SCATTER PLOT
for k, dimension in enumerate(myList):
    plt.subplot(4, 4, k)
    axes = plt.gca()
    axes.set_xlim([-maxXRange,maxXRange])
    axes.set_ylim([-maxYRange,maxYRange])
    plt.scatter(dxPlot[k], dyPlot[k], c = [.25,.75], s=25)
plt.show()