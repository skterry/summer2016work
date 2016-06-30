#SCRIPT TO VIEW MOTIONS OF FIRST 16 STARS

import sys, random
import matplotlib.pyplot as plt

ALPHA = 1
DXJITTER = -3.36688
DYJITTER = 1.28508

maxXRange = 0
maxYRange = 0
dx = []
dy = []
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
    dx.append(float(args[2])-DXJITTER)
    dy.append(float(args[3])-DYJITTER)
    totalMatches+=1
    
randomSamples = random.sample(xrange(totalMatches), 16)

for curIndex in randomSamples:
    curdx = dx[curIndex]
    curdy = dy[curIndex]
    
    if curdx/2 > maxXRange:
        maxXRange = curdx/2
    if curdy/2 > maxYRange:
        maxYRange = curdy/2
    
    dxPlot.append([-curdx/2, curdx/2])
    dyPlot.append([-curdy/2, curdy/2])
    
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