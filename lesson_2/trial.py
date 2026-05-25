# Your code goes here

def compute_sum(number):
    return sum(range(1,number + 1))

def compute_prod(number):
    result = 1
    for i in range(1 , number + 1):
        result *= i
    return result

def invalid_number(number_str):
    try:
        int(number_str)
    except(ValueError, TypeError):
        return True
    
    return False

def get_number():
    while True:
        number = input("Plase enter an integer greater than 0: ")
        if not invalid_number(number):
            return int(number)
        print('Please introduce a valid number')

def get_operation():
    while True:
        operation = input('Enter "s" to compute the sum, or "p" to compute the product. ')
        if operation in ['s', 'p']:
            return operation
        print('Please enter a valid operation')

number = get_number()
operation = get_operation()

if operation == 's':
    print(f"The sum of the integers between 1 and {number} is {compute_sum(number)}")
        
elif operation == 'p':
    print(f"The product of the integers between 1 and {number} is {compute_prod(number)}")

