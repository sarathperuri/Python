# Open (or create) a text file in write mode
file = open("example.txt", "w")

# Write some content to the file
file.write("Hello! This is a sample text file.\n")
file.write("You can write multiple lines using write().\n")
file.write("This is another line in the file.\n")

# Close the file to save changes
file.close()

print("Content written to 'example.txt' successfully.")
