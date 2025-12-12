from itertools import product


def gcd(a: int, b: int) -> int:
    """
    Finds the Greatest common divisor between two numbers
    """

    if b == 0:
        return a
    else:
        return gcd(b, a % b)


class Fraction:
    def __init__(self, num: int, den: int) -> None:
        self.numerator = num
        self.denominator = den

    def simplify(self) -> "Fraction":
        n = gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // n, self.denominator // n)

    def __eq__(self, other: "Fraction"):
        f1 = self.simplify()
        f2 = other.simplify()
        return (f1.numerator == f2.numerator) and (f1.denominator == f2.denominator)

    def __mul__(self, other: "Fraction"):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __repr__(self):
        return f"({self.numerator} / {self.denominator})"

    def __str__(self):
        return self.__repr__()


def to_n(digits: tuple[int, ...] | list[int]) -> int:
    return int("".join(str(d) for d in digits))

def get_digits(n: int) -> list[int]:
    return [int(d) for d in str(n)]


digits = (1, 2, 3, 4, 5, 6, 7, 8, 9)
number_permutations = [to_n(p) for p in product(digits, repeat=2)]

winners = []
for num in number_permutations:
    for den in [n for n in number_permutations if set(get_digits(n)).intersection(set(get_digits(num))) and n > num]:
        f = Fraction(num, den)
        shared_digit = set(get_digits(num)).intersection(set(get_digits(den))).pop()
        f_cancelled = Fraction(
            int(str(f.numerator).replace(str(shared_digit), '', 1)),
            int(str(f.denominator).replace(str(shared_digit), '', 1))
        )
        if f == f_cancelled:
            winners.append(f)

print(winners)
answer = Fraction(1,1)
for w in winners:
    answer *= w

print(answer, answer.simplify(), answer.simplify().denominator)
