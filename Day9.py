import random
n=random.randint(1,100)
flag=True
while flag:
	array=[]
	for i in range(n):
		row=[]
		for j in range(n):
			row.append(random.randint(-9,9))
		array.append(row)
	flag = all(i ==0 for i in range(len(array)))
print(array)