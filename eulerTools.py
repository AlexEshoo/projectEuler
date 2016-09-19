## eulerTools.py                                   ##
## Set of functions useful for multiple solutions. ##
from math import *

f = open('first10000primes.txt')
global _primeList
_primeList = []
for line in f:
	_primeList.append(int(line))
f.close()

def isPrime(n):
	"""
	Stolen from 0007_overview
	Author 'hk'
	"""
	if n == 1:
		return False
	elif n < 4:
		return True
	elif n % 2 == 0:
		return False
	elif n < 9:
		return True
	elif n % 3 == 0:
		return False
	else:
		r = int(floor(sqrt(n)))
		f = 5
		while f <= r:
			if n % f == 0: return False
			if n % (f+2) == 0: return False
			f += 6
		return True
	
def triangleNumber(n):
	## Arithmetic Series
	return n*(n+1)/2
	
def getFactors(num):
	if num > 1:
		factors = [1,num]
		
		#end = int(round(sqrt(num))) #Only need to go up to sqrt of number
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

def isPermutation(n,m):
	if n == m: return False
	for l in str(n):
		if l not in str(m):
			return False
	for l in str(m):
		if l not in str(n):
			return False
	return True
			

