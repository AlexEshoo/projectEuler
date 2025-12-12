from math import floor, sqrt
from itertools import permutations, cycle


def isPrime(n):
    """
    Stolen from 0007_overview
    Author 'hk'
    """
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = int(floor(sqrt(n)))
        f = 5
        while f <= r:
            if n % f == 0: return False
            if n % (f + 2) == 0: return False
            f += 6
        return True


def gen_primes():
    """
    Generator object to generate infinite sequence of primes.
    :return:
    """

    n = 1
    while True:
        while not isPrime(n):
            n += 1

        yield n
        n += 1


def digits(n: int) -> list[int]:
    return [int(d) for d in str(n)]


def number_rotations(n: int) -> list[int]:
    digit_cycle = cycle(digits(n))
    n_digits = len(digits(n))
    rotations = [n]
    for i in range(n_digits - 1):
        next(digit_cycle)  # Skip a digit
        rotations.append(int("".join([str(next(digit_cycle)) for _ in range(n_digits)])))

    return list(set(rotations))  # Remove duplicates

def is_circular_prime(n: int) -> bool:
    return all(isPrime(m) for m in number_rotations(n))

# n = gen_primes()
primes = gen_primes()
n = next(primes)
circular_primes = [n]  # start with 2
composite_digits = {0, 2, 4, 6, 8}
while n < 1e6:
    n = next(primes)
    digs = digits(n)
    if set(digs).intersection(composite_digits):
        continue

    if is_circular_prime(n):
        circular_primes.append(n)


print(len(circular_primes))
