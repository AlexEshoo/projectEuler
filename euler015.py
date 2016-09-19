from eulerTools import *
import numpy as np
import random as rand

## My Monte Carlo Solution did not work :( took way too long.
## I knew there was a way to do it with comninatorials I just needed some help.

# nodeDim = (21,21)

# arr = np.ones(nodeDim)

# for i in range(nodeDim[0]):
	# for j in range(nodeDim[1]):
		# arr[i,j] = i + float('0.'+str(j+1)) + 1

# #print arr

# paths = []

# curPos = 1.1
# row = 0
# col = 0

# count = 0
# path = [1.1]
# N=0
# while N < 5000000:
	# N += 1
	# dir = rand.randint(0,1)
	# if arr[row,col] == arr[-1,-1]:
		# if path not in paths:
			# paths.append(path)
		# else:
			# count += 1
		# path = [1.1]
		# col = 0
		# row = 0
	# elif row < nodeDim[0]-1 and dir == 0:
		# row += 1
		# path.append(round(arr[row,col],1))
	# elif col < nodeDim[1]-1 and dir == 1:
		# col += 1
		# path.append(round(arr[row,col],1))
	# else:
		# continue
		
# print len(paths)
	
# print N
# print count



# Combinatorial Sum solution
ans = 1
for i in range(0,20):
	ans *= (2 * 20) - i
	ans /= i + 1

print ans

