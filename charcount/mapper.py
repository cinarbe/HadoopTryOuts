import sys
from re import sub

for line in sys.stdin:
    line = sub(r'[^\w]','',line)
    
    for c in line.strip().lower():
        print ("%s\t%d" % (c, 1))
    
