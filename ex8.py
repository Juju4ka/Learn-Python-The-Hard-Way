# Assigns string with %r formatter operators
formatter = "%r %r %r %r"

# Replaces all %r in formatter string with data in parentheses
# Prints result
print formatter % (1, 2, 3, 4)

# Replaces all %r in formatter string with data in parentheses
# Prints result
print formatter % ("one", "two", "three", "four")

# Replaces all %r in formatter string with data in parentheses
# Prints result
print formatter % (True, False, False, True)

# Replaces all %r in formatter string with data in parentheses
# Prints result
print formatter % (formatter, formatter, formatter, formatter)

# Replaces all %r in formatter string with data in parentheses
# Prints result
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)