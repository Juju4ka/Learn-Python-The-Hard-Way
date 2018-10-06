# Import argument variable from system module
from sys import argv

# Assign data given in argument variables
# to "script" and "input_file" variable
script, input_file = argv

# Reads the file given 
# And prints it's content on the screen
def print_all(f):
	print f.read()

# Moves to the beginning of the file
def rewind(f):
	f.seek(0)

# Outputs the number of the line file reads
def print_a_line(line_count, f):
	print line_count, f.readline()

# Open file
current_file = open(input_file)

# Prints text specified in quotes
print "First let's print the whole file: \n"

# Prints the content of the file
# on the screen
print_all(current_file)

# Prints text specified in quotes
print "Now let's rewind, kind of like a tape."

# Moves to the beginning of the file
rewind(current_file)

# Prints text associated with the file
print "Let's print three lines:"

# Set current line as first one
current_line = 1

# Prints the number of the line read from a file
print_a_line(current_line, current_file)

# Increase current line number by 1
# Now current_line is equal 2
current_line = current_line + 1

# Prints the number of the line read from a file
print_a_line(current_line, current_file)

# Increase current line number by 1
# Now current_line is equal 3
current_line = current_line + 1

# Prints the number of the line read from a file
print_a_line(current_line, current_file)