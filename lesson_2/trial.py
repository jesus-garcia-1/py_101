a = 1  # first level variable
b= 5

def foo():  # second level
    b = 2

    def bar():  # third level
        c = 3
        print(a)  # => 1
        print(b)  # => 2
        print(c)  # => 3

    bar()

    print(a)  # => 1
    print(b)  # => 2
    print(c)  # => NameError: name 'c' is not defined

foo()