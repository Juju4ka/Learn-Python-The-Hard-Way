# Adds two numbers
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

# Subtracts two numbers
def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

# Multiplies two numbers
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

# Divides two numbers
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

# Prints text specified in quotes into output
print "Let's do some math with just functions!"

# Calculates age
age = add(30, 5)

# Calculates height
height = subtract(78, 4)

# Calculates weight
weight = multiply(90, 2)

# Calculates IQ
iq = divide(100, 2)

# Prints age, height, weight and IQ into output
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it anyway.
print "Here is a puzzle."

# Calcualtes some formula
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# Prints results of the calculation of the formula
print "That becomes: ", what, "Can you do it by hand?"