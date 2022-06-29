def wordCheker(phrase):
    # We split phrase into words and remove duplicates
    words = list(dict.fromkeys(phrase.split())) 
    repetitions = []
    for i in words:
        if phrase.count(i) > 1:
            repetitions.append([i, phrase.count(i)])
    return repetitions

print(*wordCheker("yes yes bye good okay bye okay bye"))