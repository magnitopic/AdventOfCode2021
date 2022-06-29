word = (input("What is the word: ") or "BANANA").upper()
vowels = ["A", "E", "I", "O", "U"]
StuartScore,KevinScore = 0,0
# Stuart's points
for i in range(len(word)):
    if word[i] not in vowels:
        StuartScore += len(word[i:])

# Kevin's points
for i in range(len(word)):
    if word[i] in vowels:
        KevinScore += len(word[i:])

if StuartScore > KevinScore:
    print(f"Stuart {StuartScore}")
elif KevinScore > StuartScore:
    print(f"Kevin {KevinScore}")
else:
    print(f"Draw")
