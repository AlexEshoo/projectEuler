def rectangle_count(n, m):
    return 0.25 * (n**2 + n) * (m**2 + m)


result = 0
target = 2000000
current = target
current_winner = (None, None)

for i in range(1, 1000):
    j = 0
    result = 0
    while result < target:
        result = rectangle_count(i, j)
        if abs(target - result) < current:
            current_winner = (i, j)
            current = abs(target-result)
        j += 1

print(current_winner, current)

print("answer:", current_winner[0] * current_winner[1])
