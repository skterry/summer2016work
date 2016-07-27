import sys

OUTPUTNAME = '.out'
INPUTNAME = ""
#
input = open(INPUTNAME)
outputString = ""

for line in input:
    args = line.split()
    
    if args[15] != "99.999" and args[28] != "99.999" and args[41] != "99.999":
        outputString+="{0} {1} {2} {3} {4} {5} {6} {7} {8}\n".format(args[2], args[3], args[10], args[15], args[23], args[28], args[36], args[41], args[49])
	
        
with open (OUTPUTNAME, 'a') as f: f.write (outputString) 