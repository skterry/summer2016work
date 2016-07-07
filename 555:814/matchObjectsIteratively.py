import sys
from decimal import Decimal

OUTPUTNAME = 'matchedStars.out'

file1 = open('F555-814chip1.out')
file2 = open('F8142012chip1.out')

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
    
curIndex = 0
for line in file2:
    curStar = lineToStar(line)
    curStar.append(curIndex)
    file2StarsList.append(curStar)
    curIndex+=1

totalStars = len(file1StarsList)        
for star1 in file1StarsList:
    if star1[8] %100 == 0:
        print("processing star {0} of {1}".format(star1[7], totalStars))
    for star2 in file2StarsList:
        if star1[5]*(1-TOLERANCE) < star2[3] < star1[5]*(1+TOLERANCE):
            if star1[0]+1<star2[0]<star1[0]+5:
                if .5<star1[1]-star2[1]<2.5:
                    dx = round(star1[0]-star2[0], 4)
                    dy = round(star1[1]-star2[1], 4)
                    with open (OUTPUTNAME, 'a') as f: f.write ("{0} {1} {2} {3} {4}\n".format(star1[8], star2[5], dx, dy, star1[7])) 
                    break
                    
