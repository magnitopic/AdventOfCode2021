import random

n = 3
MainDiagonal, SecondDiagonal, array = 0, 0, []

for i in range(n):
    row = []
    for j in range(n):
        # Value is randomlly chosen beteen -9 and 9, with diferent probability
        row.append(random.randint(1, 9))
        # Value is has a 50/50 chance of beeing negative
        if random.random() > .5:
            row[j] *= -1
    array.append(row)
print(array)
MainDiagonal += sum(array[i][i] for i in range(len(array)))
print()
for i in range(len(array)):
    print(array[i][(len(array)-1)-i])
    SecondDiagonal += array[i][(len(array)-1)-i]

print(f"Main diagonal: {MainDiagonal}")
print(f"Secondary diagonal: {SecondDiagonal}")
print(f"Absolute value of the difference: {abs(MainDiagonal-SecondDiagonal)}")
