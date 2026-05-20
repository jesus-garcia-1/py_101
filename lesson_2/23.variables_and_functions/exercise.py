#  Let’s switch to a short applied coding task:

# Write a function append_exclamation that:

#     takes a single string argument text
#     returns a new string that is text with an exclamation mark added at the end
#     does not mutate any existing object (just uses concatenation and return)

# Then show how you would:

#     Define the function
#     Invoke it with the string "Hello" and assign the result to a variable shouted
#     Print shouted

# You don’t need to explain, just write the code. 


def append_exclamation(my_string):
    return my_string + "!"

shouted = append_exclamation('Hello')
print(shouted)