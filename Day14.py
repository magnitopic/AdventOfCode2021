import numpy as np
import random

charecters = ["a", "b", "c", "d", "e", "f", "g", "h", "#", "@"]

list = []
for i in range(20):
    rnd = random.random()
    if rnd < .45:
        list.append(random.randint(0,100))
    elif .45 < rnd and rnd < .80:
        list.append(charecters[round(rnd*10)])
    elif rnd > .80:
        list.append(bool(round(rnd*10) % 2))
print(list)

ints,strs,bools=[],[],[]
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