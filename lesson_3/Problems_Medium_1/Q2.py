def factors(number):
    if number < 0:
        return 'The number must be > 0'
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(-20))