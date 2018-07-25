from sys import argv

script, filename = argv

fileObject = open(filename, 'r+')

print fileObject.read()

# Outputs text specified in quotes,
# Assigns user input to line1 variable
line1 = raw_input("line 1: ")

# Outputs text specified in quotes,
# Assigns user input to line2 variable
line2 = raw_input("line 2: ")

# Outputs text specified in quotes,
# Assigns user input to line3 variable
line3 = raw_input("line 3: ")

text = "%s\n%s\n%s\n" % (line1, line2, line3)

fileObject.write(text)

fileObject.close()