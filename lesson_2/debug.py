# Scratchpad - try out your code here
def lower_first(word):
    return word[0].lower() + word[1:]
    
    # except (TypeError, IndexError):
        # return word  # Handle exceptions by returning `word` as-is

print(lower_first("FOO"))  # Output: "fOO"
print(lower_first(32))     # Output: "32"
