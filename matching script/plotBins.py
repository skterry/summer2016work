import sys
import matplotlib.pyplot as plt

dxList = []
dyList = []
dxBin = []
dyBin = []
ALPHA = .5

matchedStarsFile = open('matchedStars.out')

print("----------------------------------------")
print("Running Script: Average, bin, aand plot")

#CALCULATE AVERAGE DX AND DY OF ALL 150K ITEMS, EXTRACTED FROM COLS 3 AND 4, RESPECTIVELY
print("Calculating average dx and dy...")
totalMatches = 0
for line in matchedStarsFile:
    args = line.split()
    dxList.append(float(args[2]))
    dyList.append(float(args[3]))
    
    totalMatches+=1

dxAverage = sum(dxList)/totalMatches
dyAverage = sum(dyList)/totalMatches

print("Average dx: {}".format(dxAverage))
print("Average dy: {}".format(dyAverage))

#1) BIN ITEMS INTO GROUPS OF 100
#2) CALCULATE DIFFERENCE BETWEEN BIN AVERAGE AND OVERALL AVERAGE
#3) PUT EACH DX AND DY INTO BINS FOR GRAPHING
print("\nBinning and creating plot...")
for i in range(int(totalMatches/100)-1):
    curdx = sum(dxList[i*100:(i+1)*100])/100
    curdy = sum(dyList[i*100:(i+1)*100])/100
    dxBin.append(curdx-dxAverage)
    dyBin.append(curdy-dyAverage)
    
#GENERATE AND DISPLAY SCATTER PLOT
plt.scatter(dxBin, dyBin, alpha=ALPHA)
ax = plt.gca() #get current axis
ax.set_ylabel('dy')
ax.set_xlabel('dy')
plt.savefig("dxdy.png")
plt.show()