import json

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f'Value must be > 0: {number_str}')
    except ValueError:
        return True
    return False


with open('calculator/file.json', 'r') as data:
    file = json.load(data)

while True:

    prompt(file["welcome"])

    prompt(file['loan_amount'])
    loan_amount = input()
    while invalid_number(loan_amount):
        prompt(file['error_number'])
        loan_amount = input()
    loan_amount = float(loan_amount)


    prompt(file['annual_rate'])
    annual_rate = input()
    while invalid_number(annual_rate):
        prompt(file['error_number'])
        annual_rate = input()
    monthly_rate = float(annual_rate) / (12 * 100 )


    prompt(file['duration'])
    duration = input()
    while invalid_number(duration):
        prompt(file['error_number'])
        duration = input()
    monthly_duration = float(duration) * 12
    monthly_payment = round(loan_amount * (monthly_rate /
                    (1 - (1 + monthly_rate) ** (-monthly_duration))),2)

    print(file['final'], monthly_payment)

    prompt('Do you want to do another calculation?')
    answer = input().lower()

    while True:
        if answer.startswith('y') or answer.startswith('n'):
            break
        prompt('Please enter "y" or "n" ')
        answer = input().lower()

    if answer[0] == 'n':
        break
