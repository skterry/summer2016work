import sys

OUTPUTNAME = 'ib3m555.out'
INPUTNAME = "ib3m13loq_flc.chip1.xym"

input = open(INPUTNAME)
outputString = ""

for line in input:
    args = line.split()
    if "#" in args[0]:
        continue
    qual = float(args[3])
    if qual >.2:
        continue
    outputString+="{0} {1} {2} {3}\n".format(args[3], args[0], args[1], float(args[7])+25.644)
        
with open (OUTPUTNAME, 'a') as f: f.write (outputString) 