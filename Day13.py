import numpy as np
leters = ["A", "G", "C", "T"]


def checkRepetitions():
    repetitions = []
    for i in range(0, len(mutation), 3):
        sequence = mutation[i:i+3]
        if mutation.count(sequence) > 1 and len(sequence) == 3:
            repetitions.append(sequence)
    return repetitions


# Create word
word = ""
for i in range(100):
    # Probability indicated by the exercise
    word += leters[np.random.choice(np.arange(0, 4), p=[.293, .207, .2, .3])]
print("Original:", word)

mutation = word
repetitions = checkRepetitions()
print("Repetitions: ", repetitions)
stop = False
# Make mutations
while len(repetitions) != 0:
    print("repetitions:", repetitions)
    sequence = list(repetitions[0])
    print(sequence)
    for j in leters:
        for i in range(len(leters)-1):
            sequence[i] = j
            # Use of ''.join() makes arrays strings of text
            if repetitions.count(''.join(sequence)) == 0:
                print("John was here")
                print(mutation)
                print(''.join(sequence))
                mutation=mutation.replace(repetitions[0], ''.join(sequence),1)
                repetitions = checkRepetitions()
                stop = True
                break
        if stop:
            break


# Binary register
# (word[i]!=mutation[i] for i in range(len(word)))
