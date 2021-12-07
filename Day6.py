def steps(n):
    matrix = []
    for i in range(n, 0, -1):
        newMatrix = []
        for j in range(i*3):
            newMatrix.append(1)
        while len(newMatrix) != n*3:
            newMatrix.append(0)
        matrix.append(newMatrix)
    return matrix


n = 3
arrays = steps(n)
for i in range(n):
    print(*arrays[i])
