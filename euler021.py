from eulerTools import *

def sumFactors(n):
	f = divisors(n)
	if n in f:
		factors = f[2:]
		return sum(factors) + 1
	else:
		return sum(f)
	
print sumFactors(220)
print sumFactors(284)

amic = []
skip = []
for n in range(2,10000):
	if n in skip: continue
	dn = sumFactors(n)
	m = dn
	if sumFactors(m) == n and n != m:
		print "Found one", n, m
		if m > n: skip.append(m)
		amic.extend([n,m])
		

print amic
print sum(amic)
	
	

