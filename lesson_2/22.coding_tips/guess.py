# Write a short snippet that represents a very simple guessing game rule:

#     The user has 3 attempts to guess a number.
#     Use a constant instead of a magic number.
#     Use clear, idiomatic variable names.

# You don’t need a full working game (no input needed); just show how you’d structure the constant and the loop that counts attempts.


SECRET_NUMBER = 5
MAX_ATTEMPTS = 3
counter = 0

while True:
    print(f'Please try to guess the secret number, you have {MAX_ATTEMPTS - counter} attempts')
    number = int(input())

    if number == SECRET_NUMBER:
        print('You guessed the secret number!')
        break

    counter += 1
    if counter >= MAX_ATTEMPTS:
        print(f"You failed your {MAX_ATTEMPTS} attempts to guess the number")
        break