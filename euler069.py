from eulerTools import getPrimeFactors, isPrime, gen_primes
import time
import json

# def totient(n):
#     if isPrime(n):
#         return n -1
#
#     primes = getPrimeFactors(n)
#     product = 1
#     for p in primes:
#         product *= 1 - (1/p)
#
#     return int(n * product)
#
# totients = {}
# prev = time.time()
# for m in range(2, 1000001):
#     if m % 10001 == 0:
#         print(m, time.time() - prev)
#         prev = time.time()
#     if not m in totients:
#         base = totient(m)
#         totients[m] = base
#         i = 2
#         while not m ** i > 1000000:
#             power = m ** i
#             totients[power] = (m ** (i-1)) * base
#             i += 1
#
# with open("outfile.json", 'w') as f:
#     json.dump(totients, f, indent=2)
#
# biggest_ratio = 0
# winner = None
# for m in totients:
#     ratio = m / totients[m]
#     if ratio > biggest_ratio:
#         biggest_ratio = ratio
#         winner = m
#
# print("Answer:", winner, biggest_ratio)


# Finesse: using Euler's formula, the ratio is maximized when prod(1-1/p) is minimized,
# Which in turn is minimized when the number of prime factors is maximized.

primes = gen_primes()
product = 1
ans = None
for p in primes:
    product *= p
    if product > 1000000:
        print("Answer", ans)
        break
    ans = product