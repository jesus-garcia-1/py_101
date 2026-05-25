


def penultimate(string):
    list_words = string.split()
    return list_words[-2]


# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")
