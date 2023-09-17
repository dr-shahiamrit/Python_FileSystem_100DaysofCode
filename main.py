# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
#

 # no longer have to rebemember to close file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write file and replace file
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# append file
with open("my_file.txt", mode='a') as file:
    file.write("\nRebemeber Amrit")

# Note: If file doesnot exit in w mode it will create file

