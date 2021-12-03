numberList=[]
for i in range(1,30,2):
	numberList.append(i)
	#print("\n")
print(numberList)
oldI=0

for i in range(1,6):
	array=[]
	for j in range(oldI,oldI+i):
		print(j)
		array.append(numberList[j])
	oldI=i
	print(f"{i}ª fila --> {array}")

'''for i in range(numberList):
	print(numberList)'''