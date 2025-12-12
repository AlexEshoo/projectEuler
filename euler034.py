from itertools import product

lut = {
    0: 1,
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
    9: 362880
}

def digits(n: int) -> list[int]:
    return [int(d) for d in str(n)]

def digit_len(n: int) -> int:
    return len(digits(n))

def factorial_sum(n: int) -> int:
    return sum(lut[d] for d in digits(n))

def number_permutations(digits: list[int], n_digits: int) -> list[int]:
    return [int("".join(str(d) for d in p)) for p in product(digits, repeat=n_digits) if p[0] != 0]

winners = []
for n_digits in range(2, digit_len(lut[9])):
    possible_digits = [n for n, v in lut.items() if digit_len(v) <= n_digits]
    candidates = number_permutations(possible_digits, n_digits)
    winners.extend([n for n in candidates if factorial_sum(n) == n])

print(winners)
print(sum(winners))
