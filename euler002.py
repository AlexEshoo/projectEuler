## Alex Eshoo && Eric Parent

## Euler 2

sum = 0
a = 1
b = 2
c = 3

while c < 4000000:
	if b % 2 == 0:
		sum = sum + b
	c = a + b
	a = b
	b = c

print sum