# Open the text file in read mode
file = open("example.txt", "r")

# Read the entire content of the file
content = file.read()

# Print the content to the console
print("File Content:\n")
print(content)

# Close the file
file.close()
