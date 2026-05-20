# So the condition if user_input: is really if "0":, which is True.

# Let’s do a small applied coding problem with this idea.

# Write a short snippet (you can just type the code, no need to run it) that:

#     Asks the user for a number.
#     Safely tries to convert it to int.
#     If conversion works, prints "Valid number" and the integer.
#     If conversion fails, prints "Invalid input".

# Use try / except and int().


number = input('Introduce a number ')

try:
    transform_number = int(number)
    print('Valid number:', transform_number)

except (ValueError, TypeError):
    print('Invalid input')