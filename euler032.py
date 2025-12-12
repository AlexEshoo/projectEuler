from itertools import permutations, combinations


# n x n = nnnnnnn  (9 x 8     = 72   never possible)
# n x nn = nnnnnn  (9 x 87    = 783  never possible)
# nn x nn = nnnnn  (98 x 76   = 7448 never possible)
# nn x nnn = nnnn  (98 x 765  = 74970 possible but there's an upper bound somewhere)
# nnn x nnn = nnn  (123 x 456 = 56088 never possible)


def to_n(digits: tuple[int, ...] | list[int]) -> int:
    return int("".join(str(d) for d in digits))


digits = (1, 2, 3, 4, 5, 6, 7, 8, 9)
pandigital_permutations = list(permutations(digits))

pandigital_identites = []
pandigital_products = set()

for p in pandigital_permutations:
    for x_ind in range(7):
        for e_ind in range(4 - x_ind):  # limit solution space based on number of digits
            multiplicand = to_n(p[:x_ind + 1])
            multiplier = to_n(p[x_ind + 1:e_ind + x_ind + 2])
            product = to_n(p[e_ind + x_ind + 2:])
            if multiplicand * multiplier == product:
                pandigital_identites.append(f"{multiplicand} x {multiplier} = {product}")
                pandigital_products.add(product)

from pprint import pprint

pprint(pandigital_identites)
print(pandigital_products)
print(sum(pandigital_products))
