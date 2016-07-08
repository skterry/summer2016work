import sys

OUTPUTNAME = 'matchedStarsBranches.out'
INPUTNAME = "matchedStarsMerged.out"

LEFTBOUND = 1.91
RIGHTBOUND = 2.09
LOWERBOUND = 17.8

input = open(INPUTNAME)
outputString = ""

for line in input:
    args = line.split()
    
    #ONLY EXTRACT COLUMN FEATURES FOR BRANCHES
    magnitude = float(args[5])
    color = float(args[4])
    if (magnitude < LOWERBOUND) and (color < LEFTBOUND or color > RIGHTBOUND):
        outputString+=line
        
with open (OUTPUTNAME, 'a') as f: f.write (outputString) 