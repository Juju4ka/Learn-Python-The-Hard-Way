from sys import argv
from os.path import exists
from os.path import getsize

script, from_file, to_file = argv

# Open file to read
in_file = open(from_file)

# Read the file
indata = in_file.read()

exists(to_file)

# Open file to write
out_file = open(to_file, 'w')

# Write data into the file
out_file.write(indata)

# Close files
out_file.close()	

in_file.close()

print """The size of the 
		input file: %r bytes, 
		output file: %r bytes""" % (getsize(from_file), getsize(to_file))