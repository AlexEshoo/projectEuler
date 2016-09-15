from eulerTools import triangleNumber

factors = 0
n = 0

while 1:
	num = triangleNumber(n)
	factors = 0
	
	for i in range(1,num+1):
		if num % i == 0:
			factors += 1
	
	if factors > 500:
		break
	
	
	print num, factors
	n += 1

print num
