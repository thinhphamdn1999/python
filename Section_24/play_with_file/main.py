# Description: This program reads the contents of a file and prints it to the console.
with open("/home/thinh-pham/Documents/python/Section_24/my_file.txt") as file:
    contents = file.read()
    print(contents)

# with open("new_file.txt", mode="w") as file:
#     file.write("\nNew text.")
