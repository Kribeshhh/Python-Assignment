def find_longest_word(file_path):
    with open(file_path, "r") as file:
        words = file.read().split()

    return max(words, key=len)

file_name = input("Enter file name: ")

print("Longest Word:", find_longest_word(file_name))