def get_digits(n):
    string = str(n)
    return list(string)


solutions = []
for n in range(2, 1000000):
    di = get_digits(n)
    # Overcomplicated it because I tried to write the sum on paper as:
    # \sum_{i=0}^m (d_i^5 - d_i\times 10^{m-i}) = 0
    result = sum( [int(d) ** 5 - int(d) * 10 ** (len(di) - i - 1) for i,d in enumerate(di)])
    if result == 0:
        solutions.append(n)

print("Answer", sum(solutions))
