import sys
from decimal import Decimal

OUTPUTNAME = 'matchedStars555-814.out'

file1 = open('ib3m814.out')#open('ibom13suq_flc.chip1.out')
file2 = open('ib3m555.out')#open('ib3m13lcq_flc.chip1.out')

TOLERANCE = .1

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
   # returningStar[3]=10**(returningStar[3]/-2.5)
    return returningStar
    
curIndex = 0
for line in file1:
    curStar = lineToStar(line)
    curStar.append(curIndex)
    file1StarsList.append(curStar)
    curIndex+=1
    #FEATURES ARE 0-qual, 1-xpos, 2-ypos, 3-mag
        
curIndex = 0
for line in file2:
    curStar = lineToStar(line)
    curStar.append(curIndex)
    file2StarsList.append(curStar)
    curIndex+=1

totalStars = len(file1StarsList)        
for star1 in file1StarsList:
    if star1[4] %100 == 0:
        print("processing star {0} of {1}".format(star1[4], totalStars))
    for star2 in file2StarsList:
        if star1[3]*(1-TOLERANCE) < star2[3] < star1[3]*(1+TOLERANCE):
            if star1[1]-2<star2[1]<star1[1]+2:
                if -2<star1[2]-star2[2]<2:
                    dx = round(star1[1]-star2[1], 4)
                    dy = round(star1[2]-star2[2], 4)
                    with open (OUTPUTNAME, 'a') as f: f.write ("{0} {1} {2} {3} {4} {5} {6} {7}\n".format(star1[4], star2[4], dx, dy, star1[3], star2[3]-star1[3], star1[1], star1[2])) 
                    file2StarsList.remove(star2)
                    break
                    
