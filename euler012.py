from eulerTools import *

factors = 0
n = 2

while True:
	num = triangleNumber(n)

	if str(num)[-1] != '0' or num % 12 != 0:
		n += 1
		continue
	
	factors = proper_divisors(num)
	
	if len(factors) > 500:
		break
	
	
	if len(factors) > 200: print n, num, len(factors)
	n += 1

print n, num, len(factors)

### Answer is 76576500 (12375th triangle number, 576 factors)
