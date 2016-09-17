
def collatzStep(n):
	if n % 2 == 0:
		return n/2
	else:
		return 3*n + 1
		
seqLens = {}

for i in range(2,1000000):
	count = 1 # 1 will always be in it, but unaccounted for by loop
	num = i
	while num != 1:
		count += 1
		num = collatzStep(num)
		if num in seqLens:
			count = count + seqLens[num]
			break
	
	seqLens[i] = count
	
largest = 0
win = None
for key in seqLens:
	if seqLens[key] > largest:
		largest = seqLens[key]
		win = key

print win, seqLens[win]