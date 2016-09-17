## Alex Eshoo && Eric Parent
## Euler 3

fuckingwot = 600851475143
blazorXprime = -1

i = 2
while i < fuckingwot:
	if fuckingwot % i == 0:
		fuckingwot = fuckingwot/i
		check = 1
		for j in range(2,i):
			if i % j == 0:
				check = 0
				break
		if check:
			blazorXprime = i
		continue
			
	i = i + 1

	if i == fuckingwot:
		blazorXprime = i
		break

print blazorXprime