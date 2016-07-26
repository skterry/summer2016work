import sys
import matplotlib.pyplot as plt
import numpy as np

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

print("----------------------------------------")
print("Running Script: Average, bin, and plot")

print("\nLoading dx and dy.............")
totalMatches = 0
for line in matchedStarsFile:
    args = line.split()
    dxList.append(float(args[4]))
    dyList.append(float(args[5]))
    totalMatches+=1

irdDX = -3.36777
irdDY = 1.19223


print("\nBinning.............")
numBins = int(totalMatches/BINSIZE)
radius = 1
for i in range(numBins):
	sys.stdout.write("\r{0}%".format(100*i/numBins+1))
	sys.stdout.flush()
	curdx = sum(dxList[i*BINSIZE:(i+1)*BINSIZE])/BINSIZE
	curdy = sum(dyList[i*BINSIZE:(i+1)*BINSIZE])/BINSIZE

	plotX = curdx-irdDX
	plotY = curdy-irdDY
	if plotX**2+plotY**2<radius:
		dxBin.append(plotX/.08)
		dyBin.append(plotY/.08)
    
       
print("\n\nCreating plot.............")    
#GENERATE AND DISPLAY SCATTER PLOT
plt.scatter(dxBin, dyBin, s=30, alpha=ALPHA)
ax = plt.gca() #get current axis
ax.set_ylabel(r'$\mu_b $, mas/yr')
ax.set_xlabel(r'$\mu_l $, mas/yr')

ax.invert_xaxis()
plt.title('Vector Point Diagram')
plt.savefig(IMAGEOUT)
plt.show()