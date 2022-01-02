import random

n = int(input("Size of the array: "))
MainDiagonal, SecondDiagonal, array = 0, 0, []

# We generate the square array
array = [[random.randint(1, 9) for i in range(n)]for j in range(n)]

# Now we figure out the two diagonals
MainDiagonal += sum(array[i][i] for i in range(n))
MainDiagonal += sum(array[i][(n-1)-i] for i in range(n))

print(array)
print(f"Main diagonal: {MainDiagonal}")
print(f"Secondary diagonal: {SecondDiagonal}")
# To get the asbsolut value of the difenence we subtract the numbers and use abs()
print(f"Absolute value of the difference: {abs(MainDiagonal-SecondDiagonal)}")
