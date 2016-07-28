import sys

OUTPUTNAME = 'F814.out'
INPUTNAME = "F814WChip1Output"
#F160Woutput
input = open(INPUTNAME)
outputString = ""

for line in input:
    args = line.split()
    
    if args[10] == "1" and args[15] != "99.999":
        outputString+="{0} {1} {2} {3} {4}\n".format(args[2], args[3], args[10], args[15], args[23])
	
        
with open (OUTPUTNAME, 'a') as f: f.write (outputString) 