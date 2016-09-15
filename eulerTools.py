## eulerTools.py                                   ##
## Set of functions useful for multiple solutions. ##

def isPrime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
			
	return True
	
def triangleNumber(n):
	## Arithmetic Series
	return n*(n+1)/2