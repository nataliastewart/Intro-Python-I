"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

fr = open("foo.txt", "r")
text = fr.read()
print(text)
fr.close()
    



# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

fw = open("bar.txt", "w")
fw.write('Hello, my name is Natalia\n')
fw.write('I am learning how to code Python\n')
fw.write('Create this file for me.\n')
fw.close()

print("-----------------------------")
fr2 = open("bar.txt", "r")
text = fr2.read()
print(text)
fr2.close()