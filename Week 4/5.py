def convert_to_uppercase(strings):
    return list(map(lambda x: x.upper(), strings))

words = input("Enter words separated by spaces: ").split()

result = convert_to_uppercase(words)

print("Uppercase Words:", result)