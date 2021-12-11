import random
import numpy
# n=random.randint(1,5)
n = 5
flag1, flag2 = True, True
while flag1:  # or flag2:
    array = []
    for i in range(n):
        row = []
        for j in range(n):
            value = (numpy.random.choice(numpy.arange(0, 10),p=[.25, .2, .16, .12, .09, .07, .05, .03, .02, .01]))
            if random.random() > .5:row.append(-value)
            else:row.append(value)
        array.append(row)
    flag1 = all(j == 0 for i in range(n) for j in array[i])
    #arrayVuelto=([[k] for i in range(n)for j in range(n)for k in range(n)])
    arrayVuelto = [array[k][i] for i in range(n)for k in range(n)]
    """ flag2 = all(j == 0 for i in range(n) for j in arrayVuelto[i]) """
    print(arrayVuelto)
print(array)
