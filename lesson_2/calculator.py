# Ask the user for first number
# Ask the user for second number
# Ask the user for an operation to perform
# Perform the operation on the two numbers
# Print the result on the terminal

import json



# Open the JSON file for reading
with open('file.json', 'r') as file:
    messages = json.load(file)

def prompt(mesage):
    print(f"===> {mesage}")

def invalid(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def message(mesage, lang='en'):
    return messages[lang][mesage]

answer = 'yes'

prompt('What language would you like to speak? (eng/esp)')
language = input()
while language not in ('eng', 'esp'):
    prompt('You should specify eng or esp')
    language = input()


prompt(message("1", language))

while answer == 'yes':
    prompt(message("2", language))
    number1 = input()

    while invalid(number1):
        prompt(message("3", language))
        number1 = input()


    prompt(message("4", language))
    number2 = input()

    while invalid(number2):
        prompt(message("3", language))
        number2 = input()

    prompt(message("5", language))

    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(message("6", language))
        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)

    prompt(f'{message("9", language)} {output}')

    prompt(message("7", language))
    answer = input()

    while answer not in ('yes', 'no'):
        prompt(message("8", language))
        answer = input()


        