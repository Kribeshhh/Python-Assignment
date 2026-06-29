def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for letter in text.lower():
        if letter in vowels:
            count += 1

    return count


text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))