from eulerTools import *


def sum_factors(k):
    fact = divisors(k)
    if k in fact:
        factors = fact[2:]
        return sum(factors) + 1
    else:
        return sum(fact)


print(sum_factors(220))
print(sum_factors(284))

amic = []
skip = []
for n in range(2, 10000):
    if n in skip:
        continue
    dn = sum_factors(n)
    m = dn
    if sum_factors(m) == n and n != m:
        print("Found one", n, m)
        if m > n:
            skip.append(m)
        amic.extend([n, m])

print(amic)
print(sum(amic))
