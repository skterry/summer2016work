import sys

OUTPUTNAME = 'ib3m13lcq_flc.chip1.out'
INPUTNAME = "ib3m13lcq_flc.chip1.xym"

input = open(INPUTNAME)
outputString = ""

for line in input:
    args = line.split()
    if "#" in args[0]:
        continue
    #ONLY EXTRACT COLUMN FEATURES FOR OBJECTTYPE=BRIGHT STAR
    #FEATURES EXTRACTED ARE XPOS, YPOS, OBJTYPE, VEGAMAG
    outputString+="{0} {1} {2} {3}\n".format(args[3], args[5], args[6], args[7])
        
with open (OUTPUTNAME, 'a') as f: f.write (outputString) 