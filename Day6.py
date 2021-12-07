def steps(n):
    matrix = []
    for i in range(n, 0, -1):
        row = []
        for j in range(i*3):
            row.append(1)
        while len(row) != n*3:
            row.append(0)
        matrix.append(row)
    return matrix


n = 4
arrays = steps(n)
for i in range(n):
    print(*arrays[i])
