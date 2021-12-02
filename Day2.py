file = open("Frankenstein.txt", "r", encoding="utf-8")
content = file.read()
characters = {}
for i in content:
    try:
        characters[i]
    except:
        characters[i] = 1
    else:
        characters[i] = characters[i] = characters[i]+1

for j in characters:
	print(f'{j} -> {characters[j]}')