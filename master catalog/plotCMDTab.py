import matplotlib.pyplot as plt
import pylab

x = []
y = []
s = 10

sepFile = open('matchedStarsFull.out')

dxAverage1 = -3.36777
dyAverage1 = 1.19223
count = 0
for line in sepFile:
    args = line.split()
    #color = float(args[2]) - float(args[3])
    color = float(args[3]) - float(args[4])#110-160
    
    dx = (float(args[5])-dxAverage1)/.08
    dy = (float(args[6])-dyAverage1)/.08
    
    #if dx >-4:
    #    continue
    
    #color = float(args[2]) - float(args[4])#814-160
    
    x.append(color)
    
    #y.append(float(args[3]))#110
    y.append(float(args[4])) #160
    count+=1

print("count: " + str(count))
    
    
plt.scatter(x, y, s=s, alpha=0.5, marker=".")
plt.title('CMD Stanek Field')
plt.xlabel('F160W - F110W')
plt.ylabel('F110W Instrumental Mag')
plt.gca().invert_yaxis()
#pylab.xlim([-0.5,5.0])

plt.show()