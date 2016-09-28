##Project Euler Problem 5##
##Alex Eshoo##



for i in range(100000000,1000000000,20): #Number must end in zero
	arr = []
	#print i
	for j in range(3,21): #all numbers will be divisible by 1 and 2
		arr.append(i%j)
	#print arr
	if i == 0:
		pass
	elif arr == 18*[0]:
		break

print i