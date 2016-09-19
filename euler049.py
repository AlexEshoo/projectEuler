
from eulerTools import *

seq = []
for n in range(1000,10000):
	if n == 1487: continue
	if isPrime(n):
		seq.append(n)
		for i in range(1,3333):
			if isPrime(n + i) and isPermutation(n, n + i):
				seq.append(n+i)
				if isPrime(seq[-1] + i) and isPermutation(seq[-1] + i, n):
					seq.append(seq[-1] + i)
					break
				else:
					seq = [n]
		if len(seq) == 3: break
		else: seq = []
		
print seq