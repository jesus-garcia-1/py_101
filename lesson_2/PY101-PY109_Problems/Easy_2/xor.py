def xor(arg1, arg2):
    return bool((not arg1 and  arg2) or (arg1 and not arg2))

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)