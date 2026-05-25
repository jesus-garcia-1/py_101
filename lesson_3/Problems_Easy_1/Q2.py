str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def search_exclamation(my_string):
    return my_string.strip().endswith('!')

print(search_exclamation(str1))
print(search_exclamation(str2))