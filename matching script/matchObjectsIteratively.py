import sys
from decimal import Decimal

OUTPUTNAME = 'matchedStars.out'

file1 = open('2010chip1cols.out')
file2 = open('2012chip1cols.out')

TOLERANCE = .05

file1StarsList = []
file2StarsList = []

if len(sys.argv) == 3:
    file1 = open(sys.argv[1])
    file2 = open(sys.argv[2])

print("----------------------------------------")
print("Running Script: Match Objects")

def lineToStar(input):
    returningStar = input.split()
    for i in range(len(returningStar)):
        returningStar[i] = float(returningStar[i])
    return returningStar
    
curIndex = 0
for line in file1:
    curStar = lineToStar(line)
    curStar.append(curIndex)
    file1StarsList.append(curStar)
    curIndex+=1
    #FEATURES ARE 0-XPOS, 1-YPOS, 2-SIGNAL-NOISE, 
    #3-OBJTYPE, 4-TOTAL COUNTS, 5-VEGAMAG, 6-SIG-NOISE(F814)
        
curIndex = 0
for line in file2:
    curStar = lineToStar(line)
    curStar.append(curIndex)
    file2StarsList.append(curStar)
    curIndex+=1
    #FEATURES ARE 0-XPOS, 1-YPOS, 2-SIGNAL-NOISE, 
    #3-OBJTYPE, 4-TOTAL COUNTS, 5-VEGAMAG, 6-SIG-NOISE(F814)

totalStars = len(file1StarsList)        
for star1 in file1StarsList:
    if star1[7] %100 == 0:
        print("processing star {0} of {1}".format(star1[7], totalStars))
    for star2 in file2StarsList:
        if star1[5]*(1-TOLERANCE) < star2[5] < star1[5]*(1+TOLERANCE):
            if star1[0]+1<star2[0]<star1[0]+4:
                if .5<star1[1]-star2[1]<2.5:
                    dx = round(star1[0]-star2[0], 4)
                    dy = round(star1[1]-star2[1], 4)
                    with open (OUTPUTNAME, 'a') as f: f.write ("{0} {1} {2} {3}\n".format(star1[7], star2[7], dx, dy)) 
                    break
                    
