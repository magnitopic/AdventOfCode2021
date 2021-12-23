import numpy as np
leters = ["A", "G", "C", "T"]


def newWord():
    # Create word
    word = ''.join([leters[np.random.choice(np.arange(0, 4), p=[.293, .207, .2, .3])]for i in range(102)])
    print(word)

    # Use of ''.join() makes arrays strings of text
    for i in range(len(word)):
        sequence = word[i:i+3]
        if word.count(sequence) > 1 and len(sequence) == 3:
            print(f"{sequence} {word.count(sequence)}")


newWord()
