from eulerTools import *

#Basic Case, pattern repeated fully each time
x = [1,2,3,4,1,2,3,4,1,2,3,4]
print getPattern(x)

# # Bsic Pattern odd length, even repititions
c = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
print getPattern(c)

# # Truncated Case Last iteration 
y = [1,2,3,4,1,2,3,4,1,2,3]
print getPattern(y, ignore_trunc = True)

# No Pattern Case
z = [1,2,3,3,44,3,21,6,8,5,2,1]
print getPattern(z)

#Truncated Case breaks pattern in last iteration
a = [1,2,3,4,1,2,3,4,1,2,2]
print getPattern(a, ignore_trunc = True)

# # Single element repeated
b = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print getPattern(b)

# Poorly defined pattern (just shy of full repeat and no established repeat)
d = [1,1,1,1,2,1,1,1,1]
print getPattern(d)
