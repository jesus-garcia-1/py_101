my_list = [1,2,3]

def mutate_function():
    my_list.append(4)

def reassign_function():
    my_list = [7,8,9]

print(my_list) #[1,2,3]
mutate_function()
print(my_list) # [1,2,3,4]
reassign_function()
print(my_list) # [1,2,3,4]