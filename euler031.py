import json
target = 200
denominations = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0] * (target + 1)
ways[0] = 1

for d in denominations:
    for j in range(d, target+1):
        ways[j] += ways[j - d]


print("Answer:", ways[-1])