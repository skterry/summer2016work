import sys

OUTPUTNAME = 'F555_814.out'
INPUTNAME = "F555-814"

input = open(INPUTNAME)
outputString = ""

for line in input:
    args = line.split()
    
    #ONLY EXTRACT COLUMN FEATURES FOR OBJECTTYPE=BRIGHT STAR
    #FEATURES EXTRACTED ARE XPOS, YPOS, OBJTYPE, VEGAMAG
    if args[10] == "1" and args[15] != "99.999" and args[28] != "99.999":
        outputString+="{0} {1} {2} {3} {4} {5} {6}\n".format(args[2], args[3], args[10], args[15], args[22], args[28], args[35])
        
with open (OUTPUTNAME, 'a') as f: f.write (outputString) 