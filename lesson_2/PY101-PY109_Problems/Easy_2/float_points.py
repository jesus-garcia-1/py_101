def prompt(message):
    print(f'==> {message}')

prompt('Enter the first number:')
first_number = float(input())
prompt('Enter the second number:')
second_number = float(input())
prompt(f'{first_number} + {second_number} = {first_number + second_number}')
prompt(f'{first_number} - {second_number} = {first_number - second_number}')
prompt(f'{first_number} * {second_number} = {first_number * second_number}')
prompt(f'{first_number} / {second_number} = {first_number / second_number}')
prompt(f'{first_number} // {second_number} = {first_number // second_number}')
prompt(f'{first_number} % {second_number} = {first_number % second_number}')
prompt(f'{first_number} ** {second_number} = {first_number ** second_number}')
