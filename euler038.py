def get_digits(n: int) -> list[int]:
    return [int(d) for d in str(n)]


def digit_len(n: int) -> int:
    return len(get_digits(n))


def to_n(digits: tuple[int, ...] | list[int]) -> int:
    return int("".join(str(d) for d in digits))


def concat_n(*nums: int) -> int:
    return int("".join(str(n) for n in nums))


def is_pandigital(n: int) -> bool:
    digits = get_digits(n)
    u_digits = set(digits)
    if 0 in u_digits:
        return (
                len(u_digits) - 1 == max(u_digits)
                and len(u_digits) == len(digits)
        )

    return (
            len(u_digits) == max(u_digits)
            and len(u_digits) == len(digits)
    )

def is_1_9_pandigital(n: int) -> bool:
    return is_pandigital(n) and min(get_digits(n)) == 1 and max(get_digits(n)) == 9

winners = []
for m in range(1, 10000):  # 9999 is a reasonable upper bound since 9999 x 1 || 9999 x 2 = 999919998
    product = m
    n = 2
    while digit_len(product) < 9:
        product = concat_n(product, m * n)
        n += 1

    if digit_len(product) == 9 and is_1_9_pandigital(product):
        winners.append(product)


print(winners)
print(max(winners))
