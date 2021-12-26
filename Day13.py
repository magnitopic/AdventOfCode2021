import numpy as np
from numpy.lib.function_base import gradient
leters = ["A", "G", "C", "T"]


# Function that creates a list of all groups of three letters that appear more than once
def checkRepetitions():
    repetitions = []
    for i in range(len(mutation)):
        sequence = mutation[i:i+3]
        if mutation.count(sequence) > 1 and len(sequence) == 3:
            repetitions.append(sequence)
    return repetitions


def getMutation(sequence):
    combinations=[[i, j, k] for i in leters for j in leters for k in leters]
    binReg=[sum([int(sequence[j] != combinations[i][j]) for j in range(3)])for i in range(len(combinations))]
    print("binReg:",binReg)
    print(min(binReg !=0))
    #for i in range(len(binReg)):
        

# Create word
word = ''.join([leters[np.random.choice(np.arange(0, 4),p=[.293, .207, .2, .3])]for i in range(102)])

# Mutates the word

mutation = word
repetitions = checkRepetitions()
while len(repetitions) != 0:
    print("repetitions:",repetitions)
    sequence = list(repetitions[0])
    print(sequence)
    options=getMutation(sequence)
    """ for i in leters:
        if mutation.count(''.join(sequence)) == 0:
            mutation = [w.replace(repetitions[0], ''.join(sequence), 1)for w in mutation]
            repetitions.pop(0)
            stop = True
            break """

print("Original:", word)
print("Mutation:", mutation)
# Binary registry
print("Binary registry", *[int(word[i] != mutation[i])for i in range(len(word))])
