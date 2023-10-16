with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("\nNew line")
    print(contents)

with open("my_new_file", mode="w") as file:
    file.write('New file')