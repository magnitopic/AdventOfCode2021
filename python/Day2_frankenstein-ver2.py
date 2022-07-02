characters = [chr(i) for i in range(32, 123)]
file = open("Frankenstein.txt", "r", encoding="utf-8").read()
[print(f"{j} => {n}") for j in characters if (n := len([i for i in file if i == j])) != 0]
