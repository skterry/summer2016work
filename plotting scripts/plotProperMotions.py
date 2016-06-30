#SCRIPT TO VIEW MOTIONS OF FIRST 16 STARS

import sys
import matplotlib.pyplot as plt

ALPHA = 1

dx = []
dy = []

dxPlot = []
dyPlot = []

star1Pos = []
star2Pos = []

starList2010 = []
starList2012 = []

DXJITTER = -3.36688
DYJITTER = 1.28508

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
    
    totalMatches+=1
    if totalMatches > 15:
        break
    
myList = ['a' for i in range(16)]
print("\n\nCreating plot.............")    
#GENERATE AND DISPLAY SCATTER PLOT
for k, dimension in enumerate(myList):
    plt.subplot(4, 4, k)
    axes = plt.gca()
    axes.set_xlim([-.5,.5])
    axes.set_ylim([-.35,.35])
    plt.scatter(dxPlot[k], dyPlot[k], c = [.25,.75], s=25)
plt.show()