import sys
from decimal import Decimal
from time import gmtime, strftime

OUTPUTNAME = 'matchedStars555-814.'
OUTPUTNAME += strftime("%Y-%m-%d.%H-%M-%S", gmtime())
OUTPUTNAME += '.out'

ib3m814 = open('ib3m814.out')
ib3m555 = open('ib3m555.out')
ibom814 = open('ibom814.out')

ib3m814List = []
ib3m555List = []
ibom814List = []

TOLERANCE = .1
MATCHBYPOS = 0
MATCHBYMAG = 1
RANGE = .5

def lineToStar(input):
    returningStar = input.split()
    for i in range(len(returningStar)):
        returningStar[i] = float(returningStar[i])
    return returningStar

def loadFile(filename):
    curIndex = 0
    returnableList = []
    for line in filename:
        curStar = lineToStar(line)
        curStar.append(curIndex)
        returnableList.append(curStar)
        curIndex+=1
    return returnableList
    #FEATURES ARE 0-qual, 1-xpos, 2-ypos, 3-mag, 4-index

def matchStarByQual(star1, matchingList):
    star1Qual = star1[0]
    star1XPos = star1[1]
    star1YPos = star1[2]
    star1Mag = star1[3]
    
    for star2 in matchingList:
        #check that qual is within tolerance:
        #if star1Qual*(1-TOLERANCE) < star2[0] < star1Qual*(1+TOLERANCE): 
        if -RANGE < star2[1]-star1XPos < RANGE: #check that x pos is within +/- .5
            if -RANGE < star2[2]-star1YPos < RANGE: #check that y pos is within +/- .5
                matchingList.remove(star2)
                color = star2[3] - star1Mag #calculate 555 mag - 814 mag
                return color
    return None
                    
def matchStarByMag(star1, matchingList):
    star1Qual = star1[0]
    star1XPos = star1[1]
    star1YPos = star1[2]
    star1Mag = star1[3]
    
    for star2 in matchingList:
        #check that magnitude is within tolerance:
        if star1Mag*(1-TOLERANCE) > star2[3] > star1Mag*(1+TOLERANCE): 
            if -5 < star1XPos-star2[1] < 1: #check that x pos is within jitter
                if .5 < star1YPos-star2[2] < 2.5: #check that y pos is within jitter
                    matchingList.remove(star2)
                    dx = star1XPos-star2[1] #calculate dx
                    dy = star1YPos-star2[2] #calculate dy
                    return (dx,dy)
    return (None, None)
    
def main():
    ib3m814List = loadFile(ib3m814)
    ib3m555List = loadFile(ib3m555)
    ibom814List = loadFile(ibom814)
    totalStars = len(ib3m814List)
    
    for ib3m814Star in ib3m814List:
        curIndex = ib3m814Star.pop(4)
        if curIndex %100 == 0:
            print("processing star {0} of {1}".format(curIndex, totalStars))
        
        #1. match objects between 814 and 555 in 2010
        curColor = matchStarByQual(ib3m814Star, ib3m555List)
        if curColor is None:
            continue
        
        #2. match objects between 2010 and 2012 in 814
        (curDx, curDy) = matchStarByMag(ib3m814Star, ibom814List)
        if curDx is None:
            continue
        
        ib3m814Star.extend([curColor, curDx, curDy])
        outputStr = " ".join(map(str, ib3m814Star))
        with open (OUTPUTNAME, 'a') as f: f.write (outputStr+"\n")

print("----------------------------------------")
print("Running Script: Match Objects")

if __name__ == "__main__":
    main()
