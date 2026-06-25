def filter_even_length_words(words):
    return list(filter(lambda x: len(x) % 2 == 0, words))

words = input("Enter words separated by spaces: ").split()

result = filter_even_length_words(words)

print("Even Length Words:", result)