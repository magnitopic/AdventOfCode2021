x = int(input("Value for X: ") or 1)
y = int(input("Value for Y: ") or 1)
z = int(input("Value for Z: ") or 2)
n = int(input("Value for N: ") or 3)
print([[i,j,k] for i in range(x+1)for j in range(y+1)for k in range(z+1)if i+j+k != n])	#Generate an array in one line
