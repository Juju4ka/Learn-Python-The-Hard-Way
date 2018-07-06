# Total number of cars
cars = 100

# Number of spaces per car
space_in_a_car = 4.0

# Total number of drivers
drivers = 30

# Total number of passengers
passengers = 90

# Number of empty cars
cars_not_driven = cars - drivers

# Number of cars available to drive
cars_driven = drivers

# Total number of passengers which can be transported
carpool_capacity = cars_driven * space_in_a_car

# Average number of spaces per car required 
# to transport all passengers
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
