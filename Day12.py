import numpy
leters = ["A", "G", "C", "T"]


def newWord():
    # Create word
    word = ""
    for i in range(100):
        # Probability indicated by the exercise
        word += leters[numpy.random.choice(numpy.arange(0, 4), p=[.293, .207, .2, .3])]
    print(word)

    # Use of ''.join() makes arrays strings of text
    for i in range(0, len(word), 3):
        sequence = word[i:i+3]
        if word.count(sequence) > 1 and len(sequence) == 3:
            print(f"{sequence} {word.count(sequence)}")


newWord()
