def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


word = input("Enter a word: ")

if is_palindrome(word):
    print("True")
else:
    print("False")