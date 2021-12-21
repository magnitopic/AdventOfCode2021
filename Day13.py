import numpy as np
leters = ["A", "G", "C", "T"]


# Function that creates a list of all groups of three letters that appear more than once
def checkRepetitions():
    repetitions = []
    for i in range(len(mutation)):
        sequence = mutation[i]
        if mutation.count(sequence) > 1:
            repetitions.append(sequence)
    return repetitions


# Create word
word = [''.join(leters[np.random.choice(np.arange(0, 4), p=[.293, .207, .2, .3])]for i in range(3))for i in range(34)]

# Mutates the word
mutation = word
repetitions = checkRepetitions()
while len(repetitions) != 0:
    sequence = list(repetitions[0])
    for j in range(len(sequence)):
        stop = False
        for i in leters:
            sequence[j] = i
            if mutation.count(''.join(sequence)) == 0:
                mutation = [w.replace(repetitions[0], ''.join(sequence), 1)for w in mutation]
                repetitions.pop(0)
                stop = True
                break
        if stop:
            break

print("Original:", *word)
print("Mutation:", *mutation)
# Binary registry
print("Binary registry", *[int(word[i] != mutation[i])
      for i in range(len(word))])
