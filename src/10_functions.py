# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(num):
    # Checks if num is even
    if num % 2 == 0:
        return True
    # Return false if odd
    else:
        return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

# If "truthy" - return first string, else return second string
print("Even!" if is_even(num) else "Odd")
