from eulerTools import isPrime, _primeList

# pos_primes = _primeList[:1000]

# neg_primes = [-p for p in pos_primes]
# neg_primes.reverse()

# print neg_primes
# primes = neg_primes + pos_primes

# a_s = primes[:]
# b_s = primes[:]

# coefs = {}

# def primeGen(n):
    # return n**2 + n + 17

# for a in [1]:
    # print a
    # for b in [17]:
        # coefs[(a,b)] = 0
        # n = 0
        # while isPrime(primeGen(n-15)):
            # #print n
            # coefs[(a,b)] += 1
            # n += 1
            
# print coefs


# def genPrime(n):
    # return n**2 + n + 17

# n = 0
# count = 0

# a = 0
# b = 0

# count_history = [0]
# while abs(a) < 1000 and abs(b) <= 1000:
    # mod = sum(count_history)
    # while isPrime(genPrime(n-mod)):
        # count += 1
        # n += 1
    
    # #print count_history
    # count_history.append(count)
    
    # a = 1 - 2*mod
    # b = mod**2 - mod + 17
    # print a, b
    
# print count_history

aMax = 0
bMax = 0
nMax = 0

primes = []

for a in range(-1000,1001):
    for b in range(-1000,1001):
        n = 0
        while isPrime(abs(n**2 + a*n + b)):
            n += 1
            
        if n > nMax:
            aMax = a
            bMax = b
            nMax = n
            
print aMax, bMax, nMax
print aMax * bMax





























