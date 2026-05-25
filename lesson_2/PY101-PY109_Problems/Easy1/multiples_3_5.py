def multisum(number):
    multiples_3 = set(range(3, number+1, 3))
    multiples_5 = set(range(5, number+1, 5))
    result = multiples_3.union(multiples_5)
    return sum(result)

print(multisum(1000))