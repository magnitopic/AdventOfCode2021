import json
# JSON changes are not saved, have to wright to the file


def printMenu():
    # Menu
    print("_"*20)
    print("Class List App")
    print(f"To interact with the information you have these options:\n\t1. Print information\n\t2. Add new information\n\t3. Edit existing information\n\t4. Delete information\n\t5. Print menu\n\t6. Exit")
    print("_"*20)


def newInfo():
    try:
        changes = int(input(
            "Would you like to...\n\t1. Add a new student\n\t2. Add new grade\nAction: "))
    except:
        print("Invalid input. Try again.")
    else:
        if changes == 1:
            name = input("Name for the new student: ")
            file[name] = {"average": None, "grades": []}
        elif changes == 2:
            name = input("Sudent's name: ")
            try:
                grade = float(input("New grade value: "))
            except:
                print("Invalid input. Try again.")
            else:
                file[name]["grades"].append(grade)
        else:
            print("Invalid input. Try again.")


def editInfo():
    try:
        changes = int(input(
            "Would you like to...\n\t1. Edit a student\n\t2. Edit a grade\nAction: "))
    except:
        print("Invalid input. Try again.")
    else:
        if changes == 1:
            name = input("Name of the student: ")
            newName = input("New name for the student: ")
            file[newName] = file.pop(name)
        elif changes == 2:
            name = input("Name of the student: ")
            try:
                position = int(input("Position of the grade: "))
                grade = float(input("New grade value: "))
                if position > len(file[name]["grades"]):
                    raise ValueError('ERROR')
            except:
                print("Invalid input. Try again.")
            else:
                file[name]["grades"][position-1] = grade
        else:
            print("Invalid input. Try again.")


def giveAverages():
    pass


def deleteInfo():
    try:
        changes = int(input(
            "Would you like to...\n\t1. Delete a student\n\t2. Delete a grade\n\t3. Delete everything\nAction: "))
    except:
        print("Invalid input. Try again.")
    else:
        if changes == 1:
            name = input("Name of the student: ")
            file.pop(name)
        elif changes == 2:
            name = input("Name of the student: ")
            try:
                position = int(input("Position of the grade: "))
                if position > len(file[name]["grades"]):
                    raise ValueError('ERROR')
            except:
                print("Invalid input. Try again.")
            else:
                del file[name]["grades"][position-1]
        elif changes==3:
            file.clear()
        else:
            print("Invalid input. Try again.")


f = open("class.json", "r")
text = f.read()

file = json.loads(text)
choice = ""
printMenu()
# file["class1"]={file["class1"],"Jeff": {"average": null,"grades": []}}
# print(file)
while choice != 6:
    try:
        choice = int(input("What do you what to do?: "))
        if 0 >= choice >= 6:
            raise ValueError('ERROR')
    except:
        print("Invalid input. Try again.")
    else:
        if choice == 1:
            print(json.dumps(file, indent=4, sort_keys=True))
        if choice == 2:
            newInfo()
        if choice == 3:
            editInfo()
        if choice == 4:
            deleteInfo()
        if choice == 5:
            printMenu()
print("Bye")
f.close()
