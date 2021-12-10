import random
n=random.randint(1,100)
array=[]
for i in range(n):
	row=[]
	for j in range(n):
		row.append(random.randint(-9,9))
	array.append(row)
print(array)