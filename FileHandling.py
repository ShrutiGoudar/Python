# Write a Python program to create a new file named “output.txt” and 
# write some string into it.

# Write a Python program to read the entire contents of a text file named 
# and print it to the console.

# Append two files

# Delete a file


def printfile(filename):        # this is similar to read file , rewriting for avoiding naming confusion while using print
    with open(filename, "r") as file:
        content = file.read()
        print(f"{filename}:")
        print(content)

def create_file(filename, content):
    with open (filename, "w") as file :
        file.write(content)
    print(f"File '{filename}' was created successfully!")

def readfile(filename):
    with open(filename, "r") as file :
        content = file.read()
        return content

def append_to_file(filename1, filename2):
    with open(filename1, "a") as file1, open(filename2, "r") as file2 :
        content = file2.read()
        file1.write(content)
    printfile(filename1)

def deletfile(filename):
    import os
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File '{filename}' deleted successfully!")
        else:
            print(f"File '{filename}' does not exist!")
    except Exception as e:
        print(f"Error deleting file '{filename}': {e}")
########################## User Defined Functions ########################
# Create files
create_file("output.txt", "Hello, This is Shruti writing to File!")
create_file("data.txt", "Deom of Append implementation")

# Read files
file_contents = readfile("output.txt")
print(f"File contains: {file_contents}")

# Append to files
# append_to_file("output.txt", "\nNew line added!")
append_to_file("output.txt", "data.txt")

# # Delete files
deletfile("output.txt")
deletfile("data.txt")
#####################################################################