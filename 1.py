def read_file_content(file_path):
    with open(file_path, "r") as file:
        return file.read()

def write_to_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

file_name = input("Enter file name: ")
content = input("Enter content to write: ")

write_to_file(file_name, content)

print("\nFile Content:")
print(read_file_content(file_name))