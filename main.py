file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

def file_read_with(file_to_read):
    with open(file_to_read) as file:
        contents = file.read()
        print(contents)

# write
with open("my_file.txt", mode='w') as file:
    file.write("Text replaced\nSecond line.\nThird line replaced.")


# append
with open("my_file.txt", mode='a') as file:
    file.write("\ntext appended.")

file_read_with("my_file.txt")


# if file not exists it will be created if in write mode
with open("new_file.txt", mode='w') as file:
    file.write("\nNew file\n")

file_read_with("new_file.txt")

with open("/Users/yordan.mirchev/Desktop/sent_file.xml") as file:
    print(file.read())

print("\nUse relative to project path: \n")
with open("../../Desktop/sent_file.xml") as file:
    print(file.read())

