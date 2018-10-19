from eulerTools import *

primes = gen_primes()


def cyclic_nums(p):
    b = 10
    t = 0
    r = 1
    n = 0
    while True:
        t = t + 1
        x = r * b
        d = int(x / p)
        r = x % p
        n = n * b + d
        if r == 1:
            break

    if t == p - 1:
        return n


prime = next(primes)  # Skip 2
winner = prime
longest = '0'

while prime < 1000:
    prime = next(primes)
    if 10 % prime == 0:
        continue
    cycle = cyclic_nums(prime)
    if cycle and len(str(cycle)) > len(longest):
        longest = str(cycle)
        winner = prime

print("Answer:", winner, len(longest))  # 983
