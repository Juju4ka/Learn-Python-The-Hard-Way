# Adds two numbers
def add(a, b):
	return a + b

# Subtracts two numbers
def subtruct(a, b):
	return a - b

# Divides two numbers
def divide(a, b):
	return a / b

# Prints text on to the output
print "Let's calculate 24 + 34 / 100 - 1023"

# Divides 34.0 by 100 
# And assign result to a quotient variable
quotient = divide(34.0, 100.0)

# Adds 24.0 to the quotient
sum = add(24.0, quotient)

# Subtructs 1023 from the sum,
# which we got on the previous step
result = subtruct(sum, 1023.0)

# Prints the result to the output
print "The result is %f" % result

# Prints text specified in quotes
print "Enter first number:"

# Reads a float number from a standard input
a = float(raw_input())

# Prints text specified in quotes
print "Enter second number:"

# Reads a float number from a standard input
b = float(raw_input())

# Prints numbers entered by user
print "You entered: %f and %f" % (a, b)

# Adds two numbers
c = add(a, b)

# Prints 2 numbers entered by user and their sum
print "The sum of %f and %f is %f" % (a, b, c)