import random
import numpy


def areThereCeros(array):
    # We loop trought all the rows
    for e in range(n):
        # Create a list of all the 0 in the row
        simple = [1 for i in range(n) if array[e][i] == 0]
        # If it's len is the same as the row the hole row made up on 0 and we return 1 to continue the loop
        if len(simple) == len(array[e]):
            return 1
    return 0


n = int(input("Give me the size of the cube: ") or 5)
flag1, flag2 = True, True
while flag1 or flag2:
    # Creates a square with same len and height
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
    # We cheek the first flag to see if a row is all ceros
    flag1 = areThereCeros(array)
    # We rotate the matrix to check the columns with the same method
    arrayGirado=[[array[k][i] for i in range(n)for k in range(n)][i*n:(i+1)*n]for i in range(n)]
    flag2 = areThereCeros(arrayGirado)
print(array)