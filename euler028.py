# Project Euler #28 Number Diagonal Sprials
# Author Alex Eshoo


def cornerNum(n,r):
    if not n in range(4):
        print "Invalid value of n"
        return None
    if r < 0:
        print "Invalid value of r"
        return None
    
    if r == 0:
        return 1
        
    else:
        return cornerNum(3,r-1) + 2*r + 2*r*n
        
sum = 1
for r in range(1,501):
    for n in range(0,4):
        
        sum += cornerNum(n,r)
        
print sum
    
