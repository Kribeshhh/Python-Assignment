class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def short_title(self):
        return self.title[:10]


books = []

for i in range(3):
    print(f"\nEnter details for Book {i+1}")
    title = input("Title: ")
    author = input("Author: ")

    books.append(Book(title, author))

print("\nShort Titles:")
for book in books:
    print(book.short_title())
    