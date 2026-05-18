# Ask the user for first number
# Ask the user for second number
# Ask the user for an operation to perform
# Perform the operation on the two numbers
# Print the result on the terminal

def prompt(message):
    print(f"===> {message}")

def invalid(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')

prompt("What's is the first number? ")
number1 = input()

while invalid(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()


prompt("What's is the second number? ")
number2 = input()

while invalid(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

prompt('''What operation would you like to perform?
1)Add 2)Substract 3)Multiply 4)Divide ''')

operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('You must choose 1, 2, 3, 4')
    operation = input()

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

prompt(f'The result is {output}')