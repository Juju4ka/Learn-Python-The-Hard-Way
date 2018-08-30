# Defines a function, 
# which prints how many  you have cheeses and crackers.
# A function takes 2 parameters 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# Prints how many cheeses you have,
	# as defined by cheese_count variable
	print "You have %d cheeses!" % cheese_count

	# Prints how many boxes of crackers you have,
	# as defined by cheese_count variable
	print "You have %d boxes of crackers!" % boxes_of_crackers

	# Prints text specified in qoutes
	print "Man that's enough for a party!"

	# Prints text specified in qoutes
	print "Get a blanket. \n"


# Prints text specified in qoutes
print "We can just give the function numbers directly:"
# Call function cheese_and_crackers
# with numbers passed as parameters
cheese_and_crackers(20, 30)

# Prints text specified in qoutes
print "OR, we can use variables from our script:"

# Initialize  amount_of_cheese variable
amount_of_cheese = 10
# Initialize  amount_of_crackers variable
amount_of_crackers = 50

# Call function cheese_and_crackers
# with variables passed as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Prints text specified in qoutes
print "We can even do math inside too:"
# Call function cheese_and_crackers
# with math passed as arguments
cheese_and_crackers(10 + 20, 5 + 6)


# Prints text specified in qoutes
print "And we can combine the two, variables and math:"
# Call function cheese_and_crackers
# with variables and math passed as arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
