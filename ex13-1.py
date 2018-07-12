from sys import argv

module_name, ingredient1, ingredient2 = argv

print "The module is: ", module_name
question = "How would you like to cook %s and %s? " % (ingredient1, ingredient2)
answer = raw_input(question)
print "I think %s is a great choice." % answer

