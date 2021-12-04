import random
array = []
pattern = random.random() < .5    # boolean
limit = random.randint(3, 15)
control = True


def detect(array):
    for i in range(len(array)):
        if ((array[i] % 2 == 0) != ((array[i-1]) % 2 == 0)) and ((array[i] % 2 == 0) != ((array[i-2]) % 2 == 0)):
            return array[i]


while len(array) < limit or control:
    number = random.randint(-99, 99)

    if (number % 2 == 0 and pattern == True) or (number % 2 != 0 and pattern == False):
        if len(array) < limit:
            array.append(number)

    elif control:
        control = False
        array.append(number)

""" random.shuffle(array) """
print(array)
print(f"The diferent number is {detect(array)}")
