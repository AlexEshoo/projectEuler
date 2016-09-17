from eulerTools import isPrime

limit = 10003 # dont know whats wrong with the indexing...
i = 1
primecount = 1

while 1: #primecount != limit:
	i += 2
	if isPrime(i): primecount += 1
	if primecount == limit: break

print i
	

