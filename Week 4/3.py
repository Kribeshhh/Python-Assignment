def check_file_empty(file_path):
    with open(file_path, "r") as file:
        return len(file.read()) == 0

file_name = input("Enter file name: ")

if check_file_empty(file_name):
    print("File is empty")
else:
    print("File is not empty")