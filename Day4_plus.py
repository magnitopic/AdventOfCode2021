numberList = []
n = int(input("How many rows?: ") or 10)        # Nº of rows
for i in range(1, n*(n+1), 2):
    numberList.append(i)

oldJ = 0
for i in range(1, n+1):
    array = []
    text = ""
    for j in range(oldJ, oldJ+i):
        if numberList[j] != 1:
            text += " + "+str(numberList[j])
        array.append(numberList[j])
        oldJ += 1
    text += " = "
    print(f"{i}ª fila ->{text[2:len(text)]}{sum(array)}")
