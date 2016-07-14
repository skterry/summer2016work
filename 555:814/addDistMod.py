import sys

INPUTNAME = 'matchedStarsBranches.out'
OUTPUTNAME = "matchedStarsDistMod.out"

input = open(INPUTNAME)
outputString = ""

for line in input:
    args = line.split()
    
    #ONLY EXTRACT COLUMN FEATURES FOR BRANCHES
    magnitude = float(args[5])
    color = float(args[4])
    M = magnitude-2*color
    dist = 10*10**((magnitude-M)/5)
    outputString+=line.rstrip()
    outputString+=" "
    outputString+=str(M)
    outputString+=" "
    outputString+=str(dist)
    outputString+="\n"
        
        
with open (OUTPUTNAME, 'a') as f: f.write (outputString) 