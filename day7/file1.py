# file = open('student.txt', 'r')
# data = file.read()
# print(data)
# file.close()

file = open('student.txt', 'w+')
file.write("This is a new line of text.\n")
file.write("This is another line of text.\n")
file.read() #This will not read anything because the file pointer is at the end of the file after writing. You need to move it back to the beginning before reading.
file.seek(0) # Move the file pointer back to the beginning of the file
data = file.read() # Now this will read the content of the file
print(data)
file.close()

# file = open('student.txt', 'r')
# data = file.read()
# print(data)
# file.close()