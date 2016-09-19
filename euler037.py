from eulerTools import *
from eulerTools import _primeList

truncPrimes = []

for i in range(1,1000000):
	if not isPrime(i) or i in [2,3,5,7]:
		continue
	for j in range(len(str(i))):
		print i
		print int(str(i)[j:]), int(str(i)[:j+1])
		if not isPrime(int(str(i)[j:])) or not isPrime(int(str(i)[:j+1])):
			break
		if j == len(str(i)) - 1: truncPrimes.append(i)
	if len(truncPrimes) == 11:
		break
		
print truncPrimes

sum = sum(truncPrimes)

print sum