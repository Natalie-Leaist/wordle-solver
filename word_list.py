class WordList:
    def __init__(self, filepath="words.txt"):
        self.words = self.load_words(filepath)

    def load_words(self, filepath):
        with open(filepath) as f:
            return [line.strip() for line in f]

    def get_words(self):
        return self.words