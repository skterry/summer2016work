import sys

OUTPUTNAME = '2012chip2cols.out'
INPUTNAME = "2012chip2output"

input = open(INPUTNAME)
outputString = ""

for line in input:
    args = line.split()
    
    #ONLY EXTRACT COLUMN FEATURES FOR OBJECTTYPE=BRIGHT STAR
    #FEATURES EXTRACTED ARE XPOS, YPOS, SIGNAL-NOISE, OBJTYPE, TOTAL COUNTS, VEGAMAG, SIG-NOISE(F814)
    if args[10] == "1" and args[15] != "99.999":
        outputString+="{0} {1} {2} {3} {4} {5} {6}\n".format(args[2], args[3], args[5], args[10], args[11], args[15], args[19])
        
with open (OUTPUTNAME, 'a') as f: f.write (outputString) 