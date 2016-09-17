## eulerTools.py                                   ##
## Set of functions useful for multiple solutions. ##
from math import *

f = open('first10000primes.txt')
global _primeList
_primeList = []
for line in f:
	_primeList.append(int(line))

def isPrime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
			return False
			
	return True
	
def triangleNumber(n):
	## Arithmetic Series
	return n*(n+1)/2
	
def getFactors(num):
	if num > 1:
		factors = [1,num]
		
		end = int(round(sqrt(num))) #Only need to go up to sqrt of number
		for i in range(2,num):
			if num % i == 0:
				factors.append(i)
	else:
		print 'Trivial, you idiot'
		
	return factors
	
def getPrimeFactors(n):
	primeFactors = {}
	for p in _primeList:
		if n % p != 0:
			break # We are done.
		crunch = n
		primeFactors[p] = 0
		while crunch % p == 0:
			primeFactors[p] += 1
			crunch = crunch / p
	return primeFactors
	
def computeDn(primeFactors):
	if len(primeFactors) == 0: return 0
	dn = 1
	for key in primeFactors:
		dn = dn*(primeFactors[key] + 1)
	return dn
	

