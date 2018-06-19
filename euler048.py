#!/bin/python3

powers = (i**i for i in range(1, 1001))
ans = str(sum(powers))[-10:]
print(ans)
