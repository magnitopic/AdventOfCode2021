from typing import Sequence
import numpy
leters = ["A", "G", "C", "T"]


def checkRepetitions():
    # Use of ''.join() makes arrays strings of text
    repetitions = []
    for i in range(0, len(word), 3):
        sequence = word[i:i+3]
        if word.count(sequence) > 1 and len(sequence) == 3:
            repetitions.append(sequence)
    return repetitions

def seeRepetition(sequence):
    return word.count(sequence)

# Create word
word = ""
for i in range(100):
    # Probability indicated by the exercise
    word +=leters[numpy.random.choice(numpy.arange(0, 4), p=[.293, .207, .2, .3])]
print("Original:",word)

mutation = word
repetitions = checkRepetitions()
print(repetitions)
# Make mutations
while repetitions != 0:
    sequence=repetitions[0]
    for j in leters:
        for i in range(len(leters)):
            if seeRepetition(sequence[j].replace(sequence[j],i,1))==0:
                replacement=sequence[j].replace(sequence[j],i,1)
                stop=True
                break
        if stop:
            break
    mutation.replace(sequence, "", 1)
    repetitions = checkRepetitions()


# Binary register
# (word[i]!=mutation[i] for i in range(len(word)))
