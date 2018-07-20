# Imports argument variable from sys module
from sys import argv

# Assigns data from command line arguments to variables
script, filename = argv

# Opens a file with specified filename
# txt is a variable holding a file object
txt = open(filename)

# Prints the name of the file
print "Here's your file %r:" % filename

# Reads all data of the file and prints it
# print txt.read()

print txt.readline()

print "The name of the file is %s" % txt.name

# Close the file
txt.close()


# Prints the text specified in quotes
print "Type the filename again:"

# Reads a string from the input and
# assigns it to a variable
file_again = raw_input("> ")

# Opens a file with specified filename and
# assigns file object to a variable txt_again
txt_again = open(file_again)

# Reads all data of the file until EOF reached
# and prints it
print txt_again.read()

# Close the file
txt_again.close()