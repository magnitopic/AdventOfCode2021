import random
NRocks = random.randint(15, 30)
print("_"*20)
print(f"Wellcome to the Nim game!\nEvery turn you'll have to take 1, 2 or 3 stones\nIf you take the last stone form the pile you loose\nYou'll play by turns against the computer\nGood Luck!! We start with {NRocks} stones")


def machineTurn(NRocks):
    m = (NRocks-1) % 4
    if m == 0:
        m = round(random.random()*3)+1
    NRocks -= m
    print(f"Machine removes {m} stones. {NRocks} remain")
    return NRocks


def humanTurn(NRocks):
    while True:
        try:
            print("_"*20)
            response = int(input("How many stones do you wnat to remove?(1, 2 or 3): "))
            if response != 1 and response != 2 and response != 3:
                raise ValueError('ERROR')
        except:
            print("Invalid input. Try again.")
        else:
            NRocks -= response
            return NRocks


while True:
    NRocks = humanTurn(NRocks)
    if NRocks <= 0:
        print(f"You removed the last stone. You lose.")
        break
    NRocks = machineTurn(NRocks)
    if NRocks <= 0:
        print(f"The machine removed the last stone. You win.")
        break
