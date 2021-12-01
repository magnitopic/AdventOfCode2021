# https://github.com/seldoncode/Python_CoderDojo/blob/main/day1.ipynb
print("I need a range of numbers")
minNum = input("The smallest number: ")
maxNum = input("The largest number: ")
try:
    minNum = int(minNum)
    maxNum = int(maxNum)
    if minNum > maxNum or minNum <= 0:
        raise ValueError('ERROR')
except:
    print("Input is not valid.")
else:
    for i in range(minNum, maxNum+1):
        numbers = []
        for j in range(1, i+1):
            if i % j == 0:
                numbers.append(j)
        print(f"{i} -> {numbers}")
