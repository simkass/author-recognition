class Word:
    def __init__(self, word: str):
        self.word = word
        self.count = 1
        self.following_words = {}

    def increment_count(self):
        self.count += 1

    def get_count(self):
        return self.count

    def add_following_word(self, word: str):
        self.following_words[word] = 1

    def increment_following_word(self, word: str):
        self.following_words[word] += 1

    def get_following_words(self):
        return self.following_words
