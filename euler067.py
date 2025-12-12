def load_triangle(path: str) -> list[list[int]]:
    rows = []
    with open(path, 'r') as f:
        for line in f:
            rows.append([int(n) for n in line.split(' ')])

    return rows

triangle = load_triangle("resources/0067_triangle.txt")

for row_i in reversed(range(len(triangle) - 1)):
    row = triangle[row_i]
    for col_i in range(len(row)):
        row[col_i] += max(
            triangle[row_i][col_i], triangle[row_i + 1][col_i + 1]
        )

print(triangle[0][0])
        