from eulerTools import isPrime, gen_primes

def get_lower_primes(n):
    primes = []
    for p in gen_primes():
        if p >= n:
            return primes

        primes.append(p)

print(get_lower_primes(41))