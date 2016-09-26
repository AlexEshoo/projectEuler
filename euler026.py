from eulerTools import *
import decimal
# Need to be able to find patterns after initial numbers in decimal like in 1/6 for example...
decimal.getcontext().prec = 500
longest = 0
longpat = []
win = None
for i in range(2, 1000):
	num = decimal.Decimal(1)/decimal.Decimal(i)
	dec = [ int(j) for j in str(num) if j != '.']
	dec = dec[1:]
	
	pat = getPattern(dec, ignore_trunc = True) # Need to ignore the truncated part since rounding error is a thing.
	if len(pat) > longest: 
		longest = len(pat)
		longpat = pat
		win = i

print longpat
print longest
print win