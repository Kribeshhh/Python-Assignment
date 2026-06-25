class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        return len(self.text.split())


text = input("Enter a text: ")

analyzer = TextAnalyzer(text)

print("Number of words:", analyzer.word_count())