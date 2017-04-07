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
	factors= []
	if num > 1:
		factors = [1,num]
		
		#end = int(round(sqrt(num))) #Only need to go up to sqrt of number
		for i in range(2,num):
			if num % i == 0:
				factors.append(i)
	else:
		factors.append(1)
		return factors
		
	return factors
	
def getPrimeFactors(n):
	primeFactors = {}
	for p in _primeList:
		if p > n:
			break
		elif n % p != 0:
			continue
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
	
def getPattern(nums, ignore_trunc = False):
	"""
	Finds a pattern (if any) in a given list.
	Some nuances: If the pattern is truncated after being well established it will still return the pattern. (assumes it will repeat)
	If the pattern is not well established, there will be nothing returned. Patterns must repeat at least once (2 sequences) before 
	one will be detected.
	
	:parameters: nums: a list of items to be parsed. Can contain (almost?) anything.
	
	:returns: pat: A list containing a single repititon of the pattern of the nums list.
	if there is no pattern pat = []
	"""
	pat = None
	pat = [nums[0]]
	while len(pat) < len(nums):
		if len(nums)/len(pat) < 2:
			return [] # Not possible to repeat anything. If list has poorly defined pattern (truncated before first repititon) this will happen
		for i in range(0,len(nums)/len(pat)):
			if nums[i*len(pat) : (i+1)*len(pat)] == pat:
				if i == len(nums)/len(pat) - 1 and (len(nums)%len(pat) == 0 or ignore_trunc == True):
					return pat
				elif i == len(nums)/len(pat) - 1 and pat[:len(nums) % len(pat)] == nums[-(len(nums) % len(pat)):]:
					return pat
				elif i == len(nums)/len(pat) - 1:
					return [] # Truncated section does not match.
				else:
					continue
			else:
				pat = nums[:len(pat) + 1]
				break
	return []
    
def gcd(a,b):
    """
    Finds the Greates common divisor between two numbers
    """
    
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
    
    
    
    
    
    