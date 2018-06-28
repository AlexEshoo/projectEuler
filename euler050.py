from eulerTools import isPrime, gen_primes
from itertools import islice

def get_lower_primes(n):
    primes = []
    for p in gen_primes():
        if p >= n:
            return primes

        primes.append(p)

def gen_lower_primes(n):
    for p in gen_primes():
        if p >= n:
            break
        yield p

def count_iterable(i):
    return sum(1 for e in i)

prime_sums = {}
primes = gen_lower_primes(1000)

num_primes = count_iterable(primes)
print(num_primes)

for i in range(num_primes):
    for j in range(num_primes - i):
        # print(i,j)
        seq = islice(gen_lower_primes(1000), i, i + j)
        s = sum(islice(gen_lower_primes(1000), i, i + j))
        # print("sum", s)
        if isPrime(s) and s < 1000:
            prime_sums[s] = j + 1

print(prime_sums)

longest = 0
p = 0
for n in prime_sums:
    if prime_sums[n] > longest:
        longest = prime_sums[n]
        p = n

print(p)
print(prime_sums[p])
