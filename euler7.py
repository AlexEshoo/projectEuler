from eulerTools import isPrime

i = 1
primecount = 0

while primecount < 10002:
	if isPrime(i):
		print i, primecount	
		primecount += 1
	i += 1