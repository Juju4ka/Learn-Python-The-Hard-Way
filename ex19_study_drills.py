import fnmatch, re

# Opens file and writes data, then closes the file
def write_data_to_file(filename, data):
	if (filename == None):
		print("Filename can't be empty")
	else:
		if (data == None):
			print("Data can't be empty")
		# Check whether filename is valid
		if(fnmatch.fnmatch(filename, "*.txt")):
			print ("Opening a file: %s" % filename)			
			fileObject = open(filename, "w")
			data_string = str(data)
			print("Writing data: %s" % data_string)
			fileObject.write(data_string)
			fileObject.write("\n")
			fileObject.close()
			print ("Closing file\n\n")
		else:
			print("Filename must be a text file.")


filename = "ex19_sample.txt"
data = "Python is cool.\n"

# 1. Passing straight text for both parameters
write_data_to_file("ex19_sample.txt", "Sample text")

# 2. Passing straight text for 1st parameter and a variable for 2nd
write_data_to_file("ex19_sample.txt", data)

# 3. Passing a variable for 1st parameter and a straight text for 2nd parameter
write_data_to_file(filename, "Study drills")

# 4. Passing variables for 1st and 2nd parameter
write_data_to_file(filename, data)

# 5. Passing a variable for 1st parameter and a number for 2nd
write_data_to_file(filename, 12345)

# 6. Passing a variable for the 1st parameter and a math for 2nd
write_data_to_file(filename, 100+200)

# 7. Passing a text combined with variable for the 1st parameter and a variable for 2nd
file_number = 1
write_data_to_file("ex19_sample%s.txt" % (file_number), data);

filenamePrefix = 10;
data2 = "HI'm happy and I love it! :) \n"

# 8. Passing a straight text for 1st parameter and a number for 2nd
write_data_to_file("ex19_sample2.txt", 12345)

# 9. Passing a text combined with variables for 1st  and 2nd parameter
write_data_to_file("%s%s.txt" % ("ex19_sample", filenamePrefix), "%s%s" % (data, data2))

# 10. Passing a variable for the 1st parameter and None for the 2nd parameter
write_data_to_file(filename, None)

# 11. Passing None for both parameters
write_data_to_file(None, None)

# 12. Passing hex value for 2nd parameter
write_data_to_file(filename, 0X7F)

# 13. Passing a binary value for 2nd parameter
write_data_to_file(filename, 0B1111111)


