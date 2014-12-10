import sys
from re import sub

for line in sys.stdin:
    
    aline = sub(r'[^\w]',' ',line)
    
    keys = aline.split()
        

    for key in keys:
        
        adjkey = key.lower().strip()
        value = 1
        
        if adjkey != '':
            print( "%s\t%d" % (adjkey, value) )
