from eulerTools import isPrime, _primeList

pos_primes = _primeList[:1000]

neg_primes = [-p for p in pos_primes]
neg_primes.reverse()

print neg_primes
primes = neg_primes + pos_primes

a_s = primes[:]
b_s = primes[:]

coefs = {}

def primeGen(n):
    return n**2 + n + 17

for a in [1]:
    print a
    for b in [17]:
        coefs[(a,b)] = 0
        n = 0
        while isPrime(primeGen(n-15)):
            #print n
            coefs[(a,b)] += 1
            n += 1
            
print coefs