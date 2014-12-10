import re

f = open("pg2701.txt","r")
charlib = {}
lines = f.readlines()


for line in lines:
    adj = re.sub("[^\w]","",line).lower()
    
    for c in adj:
        if c not in charlib.keys():
            charlib[c]=1
        else:
            charlib[c] += 1


for k in charlib.keys():
    print ("%s\t%d" % (k, charlib[k]))   
    
