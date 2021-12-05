file = open("Frankenstein.txt", "r", encoding="utf-8")
content = file.read()
characters = {}
for v in content:
    try:
        characters[v]
    except:
        characters[v] = 1
    else:
        characters[v] += 1
file.close()
for v in characters:
    print(f'{v} -> {characters[v]}')
