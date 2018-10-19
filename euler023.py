from eulerTools import is_abundant, proper_divisors

maximum = 28123

abundants = [i for i in range(1,maximum) if is_abundant(i)]
print(abundants)

abundant_sums = set()

for i, n in enumerate(abundants):
    for m in abundants[i:]:
        print(n,m)
        abundant_sums.add(n + m)

all_nums = set(range(1,maximum))

non_abundant_sums = all_nums.difference(abundant_sums)

print(abundant_sums)
print(non_abundant_sums)
print("answer:", sum(non_abundant_sums))