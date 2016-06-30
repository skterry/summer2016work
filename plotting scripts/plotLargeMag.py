import sys
import matplotlib.pyplot as plt

dxList = []
dyList = []
dxBin = []
dyBin = []
ALPHA = .5
BINSIZE = 1

IMAGEOUT = 'dxdy.png'

if len(sys.argv)==2:
    IMAGEOUT = sys.argv[1]

matchedStarsFile = open('matchedStars.out')
star1File = open('2010chip1cols.out')
magnitudeList = []

print("----------------------------------------")
print("Running Script: Average, bin, aand plot")

#CALCULATE AVERAGE DX AND DY OF ALL 150K ITEMS, EXTRACTED FROM COLS 3 AND 4, RESPECTIVELY
print("\nCalculating average dx and dy.............")
totalMatches = 0

for line in star1File:
    args = line.split()
    magnitudeList.append(float(args[5]))

for line in matchedStarsFile:
    args = line.split()
    starNum = int(args[0])
    if magnitudeList[starNum] > 18.5:
        continue
    dxList.append(float(args[2]))
    dyList.append(float(args[3]))
    
    totalMatches+=1

dxAverage = sum(dxList)/totalMatches
dyAverage = sum(dyList)/totalMatches

print("Average dx: {}".format(dxAverage))
print("Average dy: {}".format(dyAverage))

#1) BIN ITEMS INTO GROUPS OF BINSIZE
#2) CALCULATE DIFFERENCE BETWEEN BIN AVERAGE AND OVERALL AVERAGE
#3) PUT EACH DX AND DY INTO BINS FOR GRAPHING

#dxAverage = -3.36
#dyAverage = 1.28

print("\nBinning.............")
numBins = int(totalMatches/BINSIZE)-1
for i in range(numBins):
    sys.stdout.write("\r{0}%".format(100*i/numBins+1))
    sys.stdout.flush()
    curdx = sum(dxList[i*BINSIZE:(i+1)*BINSIZE])/BINSIZE
    curdy = sum(dyList[i*BINSIZE:(i+1)*BINSIZE])/BINSIZE
    dxBin.append((curdx-dxAverage)/.04)
    dyBin.append((curdy-dyAverage)/.04)
    #if dxBin[-1] < -7 or dxBin[-1]>7:
    #    dxBin.pop()
    #    dyBin.pop()

print("\n\nCreating plot.............")    
#GENERATE AND DISPLAY SCATTER PLOT
plt.scatter(dxBin, dyBin, s = 2, alpha=ALPHA)
ax = plt.gca() #get current axis
ax.set_ylabel('dy')
ax.set_xlabel('dx')
ax.invert_xaxis()
plt.savefig("dxdy.png")
plt.show()