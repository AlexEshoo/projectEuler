##Project Euler Problem 4##
##Alex Eshoo##

product = -1
palindrome = -1

def palCheck(product):
	string = str(product)
	backward = []
	forward = []
	arr = []
	for ch in string:
		arr.append(ch)
	forward = list(arr)
	arr.reverse()
	backward = arr
	#print 'forward: ', forward
	#print 'backward: ', backward
	if forward == backward:
		return product
	else: 
		return -1

for i in range(100,1000):
	for j in range(100,1000):
		product = i*j
		if palCheck(product) == -1:
			pass
		elif product > palindrome:
			palindrome = product
		else:
			pass


print palindrome