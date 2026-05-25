# Create a function that takes 2 arguments, a list and a dictionary. The list 
# will contain 2 or more elements that, when joined with spaces, will produce a 
# person's name. The dictionary will contain two keys, "title" and "occupation", 
# and the appropriate values. Your function should return a greeting that uses 
# the person's full name, and mentions the person's title.7


def greetings(list_, dictionary_):
    name = ' '.join(list_)
    title = dictionary_['title']
    occupation = dictionary_['occupation']
    return f'Hello, {name}! Nice to have a {title} {occupation} around.'

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

