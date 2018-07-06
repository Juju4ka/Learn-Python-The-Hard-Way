# Initialization of variable x
x = "There are %d types of people." % 10

# Initialization of variable binary
binary = "binary"

# Initialization of variable do_not
do_not = "don't"

# Initialization of variable y
y = "Those who know %s and those who %s." % (binary, do_not)

# Print value of x
print x

# Print value of y
print y

# Print text along with value of x
print "I said: %r." % x 

# Print text along with value of y
print "I also said: '%s'." % y

# Initialization of variable hilarious
hilarious = False

# Initialization of variable joke_evaluation
joke_evaluation = "Isn't that joke so funny! %r" 

# Print value of joke_evaluation
# where %r will be replaced with the value of hilarious
print joke_evaluation % hilarious

# Initialization of variable w
w = "This is the left side of..."

# Initialization of variable e
e = "a string with a right side."

# Prints a line made by joining w and e
print w + e