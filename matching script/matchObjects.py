import sys

file1 = open('2010chip1cols.out')
file2 = open('2012chip1cols.out')

file2StarsDict = {}

if len(sys.argv) == 3:
    file1 = sys.argv[1]
    file2 = sys.argv[2]

print("----------------------------------------")
print("Running Script: Match Objects")

def myround(x, prec=2, base=.05):
  return round(base * round(float(x)/base),prec)

def lineToStar(input):
    returningStar = input.split()
    for i in range(len(returningStar)):
        returningStar[i] = float(returningStar[i])
    return returningStar
    
curIndex = 0
for line in file2:
    curStar = lineToStar(line)
    
    #FEATURES ARE 0-XPOS, 1-YPOS, 2-SIGNAL-NOISE, 
    #3-OBJTYPE, 4-TOTAL COUNTS, 5-VEGAMAG, 6-SIG-NOISE(F814)
    
    curMag = myround(curStar[5])
    
    if curMag not in file2StarsDict.keys():
        file2StarsDict[curMag] = []
    
    file2StarsDict[curMag].append(curStar)
    
    curIndex+=1
    
for line in file1:
    curStar = lineToStar(line)
    
    #FEATURES ARE 0-XPOS, 1-YPOS, 2-SIGNAL-NOISE, 
    #3-OBJTYPE, 4-TOTAL COUNTS, 5-VEGAMAG, 6-SIG-NOISE(F814)
    
    curMag = myround(float(curStar[5]))
    
    if curMag in file2StarsDict.keys():
        potentialMatchList = file2StarsDict[curMag]
        for potentialMatch in potentialMatchList:
            print(curStar[4])
            deltaCounts = (curStar[4]-potentialMatch[4])**2
            #print(deltaCounts)
            #if deltaCounts < .05:
            #    print(deltaCounts)
                #print(curStar[0]-potentialMatch[0])
        
        
        #print(len(potentialMatchList))