
numDict = { 1 : 'one',
			2 : 'two',
			3 : 'three',
			4 : 'four',
			5 : 'five',
			6 : 'six',
			7 : 'seven',
			8 : 'eight',
			9 : 'nine',
			10 : 'ten',
			11 : 'eleven',
			12 : 'twelve',
			13 : 'thirteen',
			14 : 'fourteen',
			15 : 'fifteen',
			18 : 'eighteen',
			20 : 'twenty',
			30 : 'thirty',
			40 : 'forty',
			50 : 'fifty',
			60 : 'sixty',
			70 : 'seventy',
			80 : 'eighty',
			90 : 'ninety',
			1000 : 'onethousand'
			}

def getNumberString(n):
	if n in numDict:
		return numDict[n]
	if len(str(n)) == 2:
		if n < 20:
			return numDict[int(str(n)[1])] + 'teen'
		
		return numDict[int(str(n)[0] + '0')] + numDict[int(str(n)[1])]
	if len(str(n)) == 3:
		if str(n)[1:] == '00':
			return numDict[int(str(n)[0])] + 'hundred'
		
		return numDict[int(str(n)[0])] + 'hundredand' + getNumberString(int(str(n)[1:]))

string = ''
count = 0
for i in range(1,1001):
	tmp = getNumberString(i)
	string += tmp
	count += len(tmp)
	
print count
print len(string)