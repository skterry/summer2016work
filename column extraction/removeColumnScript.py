import sys

OUTPUTNAME = '2012F814.out'
INPUTNAME = "2012F814output"

input = open(INPUTNAME)
outputString = ""

for line in input:
    args = line.split()
    
    #ONLY EXTRACT COLUMN FEATURES FOR OBJECTTYPE=BRIGHT STAR
    #FEATURES EXTRACTED ARE XPOS, YPOS, OBJTYPE, VEGAMAG
    if args[10] == "1":
        outputString+="{0} {1} {2} {3}\n".format(args[2], args[3], args[10], args[15])
        
with open (OUTPUTNAME, 'a') as f: f.write (outputString) 