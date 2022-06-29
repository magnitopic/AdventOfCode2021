def getArray(string):
    try:
        array = [int(i) for i in string.split()]
    except:
        return "Invalid value"
    else:
        return array


def kangaroo():
    getArray("1 2 3 4")
	
