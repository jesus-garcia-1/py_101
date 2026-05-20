# Write a function add_five_in_place that:

#     Takes a list of numbers as a parameter
#     Mutates the list so that the number 5 is added at the end
#     Does not return anything (or returns None implicitly)

# Then show:

#     A list vals = [10, 20]
#     A call to add_five_in_place(vals)
#     A print that shows the mutated vals



vals = [10, 20]

def add_five_in_place(list_):
    list_.append(5)

add_five_in_place(vals)
print(vals)