from eulerTools import *

f = open('euler013.txt')
nums = []
for line in f:
	nums.append(int(line))
f.close()

sum = 0
for n in nums:
	sum += n
	
print sum
print str(sum)[:10]