# Imports argument variable from the sys module
from sys import argv

# assigns script's name and a filename from argument variables
script, filename = argv

# Prints text specified in quotes
# Replaces %r with the content of a filename variable
print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C (^C)."
print "If you do want that, hit RETURN."

# Outputs question mark 
# and waits for the input from user
raw_input("?")

# Prints text specified in quotes
print "Opening the file..."
# Opens a file with specified filename for writing
# Assigns file object to target variable
target = open(filename, 'w')

# Prints text specified in quotes
print "Truncating the file. Goodbye!"

# Erases the content of the file
target.truncate()

# Prints text specified in quotes
print "Now I'm going to ask you for three lines."

# Outputs text specified in quotes,
# Assigns user input to line1 variable
line1 = raw_input("line 1: ")

# Outputs text specified in quotes,
# Assigns user input to line2 variable
line2 = raw_input("line 2: ")

# Outputs text specified in quotes,
# Assigns user input to line3 variable
line3 = raw_input("line 3: ")


# Prints text specified in quotes
print "I'm going to write these to the file."

# Writes content of the line1 variable to a file
target.write(line1)
# Writes end of line to the file
target.write("\n")
# Writes content of the line2 variable to a file
target.write(line2)
# Writes end of line to the file
target.write("\n")
# Writes content of the line3 variable to a file
target.write(line3)
# Writes end of line to the file
target.write("\n")

# Prints text specified in quotes
print "And finally, we close it."
# Closes the file
target.close()