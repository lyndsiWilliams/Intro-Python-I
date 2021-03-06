"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

print("--- Exercise 1: ")
f = open('foo.txt', 'r')
# f.read() will print the entire block of code, but that was messy
# This for loop cleans it up!
for line in f:
    print(line, end='')
# Close the file for the OS
f.close()

# Another way to do the block of code above
# Using the with keyword will automatically do the .close() functionality
with open("foo.txt") as fp:
    for line in fp:
        print(line)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

b = open('bar.txt', 'w')
print("\n\n--- Exercise 2: (see bar.txt file)")
b.write('Line 1\nLine 2\nLine 3')
# Close the file for the OS
b.close()

# Rewriting the above code block another way
with open("bar2.txt", "w") as fp:
    fp.write('Line 1\nLine 2\nLine 3')
