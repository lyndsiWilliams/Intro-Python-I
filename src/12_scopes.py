# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12


def change_x():
    # In order to use a global variable inside a function,
    # you've got to "import" it with the global keyword
    global x
    x = 99


change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print("--- Exercise 1: ")
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        # The nonlocal keyword works similar to the global keyword,
        # except it is used for inner/outer functions
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print("--- Exercise 2: ")
    print(y)


outer()
