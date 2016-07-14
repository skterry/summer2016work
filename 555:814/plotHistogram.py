import sys
import matplotlib.pyplot as plt
import numpy
from scipy.optimize import curve_fit

dxListTotal = []
dyListTotal = []

dxListWithinRadius = []
dyListWithinRadius = []

colorList = []

diskDx = []
diskDy = []
bulgeDx = []
bulgeDy = []

IMAGEOUT = 'histogram.png'

if len(sys.argv)==2:
    IMAGEOUT = sys.argv[1]

matchedStarsFile = open('matchedStarsBranches.out')

print("----------------------------------------")
print("Running Script: Make histogram")

print("\nLoading dx and dy.............")
totalMatches = 0
for line in matchedStarsFile:
    args = line.split()
    dxListTotal.append(float(args[2]))
    dyListTotal.append(float(args[3]))
    colorList.append(float(args[4]))
    totalMatches+=1

#matlab program - chip1
dxAverage1 = -3.278
dyAverage1 = 1.283

#matlab program - chip2
dxAverage2 = -3.192
dyAverage2 = 1.384

c="""
#IRD Python Program  Chip1
dxAverage1=-3.37293888426 
dyAverage1=1.28905678601

#IRD Python Program Chip 2
dxAverage2=-3.07407676245 
dyAverage2= 1.35405712439"""

radius = 1
for i in range(totalMatches):
    curdx = dxListTotal[i]
    curdy = dyListTotal[i]
    if (i < 527):
        plotX = curdx-dxAverage2
        plotY = curdy-dyAverage2
        if plotX**2+plotY**2<radius:
            dxListWithinRadius.append(plotX/.04)
            dyListWithinRadius.append(plotY/.04)
        else:
            colorList.pop(i)
    else:
        plotX = curdx-dxAverage1
        plotY = curdy-dyAverage1
        if plotX**2+plotY**2<radius:
            dxListWithinRadius.append(plotX/.04)
            dyListWithinRadius.append(plotY/.04)
        else:
            colorList.pop(i)

diskCount = 0 #left side - dx1/dy1
bulgeCount = 0 #right side - dx2/dy2

for i in range(len(dxListWithinRadius)):
    if colorList[i] < 2.05:
        diskDx.append(dxListWithinRadius[i])
        diskDy.append(dyListWithinRadius[i])
    else:
        bulgeDx.append(dxListWithinRadius[i])
        bulgeDy.append(dyListWithinRadius[i])

# Define model function to be used to fit to the data above:
def gauss(x, *p):
    A, mu, sigma = p
    return A*numpy.exp(-(x-mu)**2/(2.*sigma**2))
    
def calcFit(data):

    hist, bin_edges = numpy.histogram(diskDx, 100, density=True)
    bin_centres = (bin_edges[:-1] + bin_edges[1:])/2

    # p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
    p0 = [1., 0., 1.]

    coeff, var_matrix = curve_fit(gauss, bin_centres, hist, p0=p0)

    # Get the fitted curve
    hist_fit = gauss(bin_centres, *coeff)
    return (hist_fit, bin_centres)


       
print("\n\nCreating plot.............")    
#GENERATE AND DISPLAY HISTOGRAM

histData = [(diskDx, bulgeDx), (bulgeDy, diskDy)]
histTitles = ['diskDx, bulgeDx', 'bulgeDy, diskDy']
for k, dimension in enumerate(histData):
    plt.subplot(2, 1, k)
    axes = plt.gca()
    
    plt.hist(dimension[0], bins=15, normed=True, histtype='step', color='r')
    (hist_fit, bin_centres) = calcFit(dimension[0])
    plt.plot(bin_centres, hist_fit, color='r')
    
    plt.hist(dimension[1], bins=15, normed=True, histtype='step', color='g')
    (hist_fit, bin_centres) = calcFit(dimension[1])
    plt.plot(bin_centres, hist_fit, color='g')
    
    ax = plt.gca() #get current axis
    ax.set_ylabel('Number')
    ax.set_xlabel(histTitles[k])

plt.savefig(IMAGEOUT)
plt.show()