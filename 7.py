def process_file_with_lambda(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

    processed_lines = []

    for line in lines:
        words = line.split()
        upper_words = list(map(lambda word: word.upper(), words))
        processed_lines.append(" ".join(upper_words) + "\n")

    with open(file_name, "w") as file:
        file.writelines(processed_lines)

file_name = input("Enter file name: ")

process_file_with_lambda(file_name)

print("File content converted to uppercase successfully.")