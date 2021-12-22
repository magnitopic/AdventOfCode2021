import random, string

charecters = list(string.ascii_letters)

list = []
for i in range(20):
    rnd = random.random()
    if rnd < .45:
        list.append(random.randint(0, 100))
    elif .45 < rnd and rnd < .80:
        list.append(charecters[random.randint(0, len(charecters)-1)])
    else:
        list.append(bool(int(rnd*10) % 2))
print(*list)

ints, strs, bools = [], [], []
for i in list:
    if isinstance(i, str):
        strs.append(i)
    elif isinstance(i, bool):
        bools.append(i)
    elif isinstance(i, int):
        ints.append(i)

print(f"Characters : {strs}")
print(f"Numbers : {ints}")
print(f"Booleans : {bools}")
