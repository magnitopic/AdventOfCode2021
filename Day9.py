import random
import numpy
# n=random.randint(1,5)


def areThereCeros(array):
    for e in range(n):
        simple = [1 for i in range(n) if array[e][i] == 0]
        if len(simple) == len(array[e]):
            return 1
    return 0


n = int(input("Give me the size of the cube: ") or 1)

flag1, flag2 = True, True
while flag1 or flag2:
    # Creates a square with same len and height
    arrayGirado = []
    array = []
    for i in range(n):
        row = []
        for j in range(n):
            # Value is randomlly chosen beteen -9 and 9, with diferent probability
            row.append(numpy.random.choice(numpy.arange(0, 10),p=[.25, .2, .16, .12, .09, .07, .05, .03, .02, .01]))
            # Value is has a 50/50 chance of beeing negative
            if random.random() > .5:
                row[j] *= -1
        array.append(row)
    flag1 = areThereCeros(array)
    for i in range(n):
        arrayGirado.append([array[k][i] for i in range(n)for k in range(n)][i*n:(i+1)*n])
    flag2 = areThereCeros(arrayGirado)
print(array)
