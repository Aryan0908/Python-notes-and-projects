# Opening up the text file
file = open("my_file.txt")

# Reading the opened file
content = file.read()
print(content)

# Closing the file
file.close()

# Sometimes we forget to close our file so we use (with) function to close our file automatically
with open("my_file.txt") as file:
    content = file.read()
    print(content)

# Writing into our file
"""
To write we have to change file mode from 'r' i.e. read only to 'w' i.e. write his will delete all the previous text
and replace it with the text we enter. To add the text without removing the previous text then we have to shift the mode
to 'a'.

If in 'w' mode we specify a file that dosen't exist then it will create a new file with that name.
"""

with open("my_file.txt", mode='a') as file:
    file.write("\nNew Text")
    # Look at the file it is added their
    
    # .readlines() it will convert every line into a list
    file.readlines()


