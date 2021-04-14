class Word:
    def __init__(self):
        self.count = 1
        self.following_words = {}

    def __iadd__(self, x):
        self.count += x

    def get_count(self):
        return self.count

    def add_following_word(self, word):
        self.following_words[word] = 1

    def get_following_words(self):
        return self.following_words
