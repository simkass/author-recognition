import os

class AuthorDictionary:
    def __init__(self, author):
        self.author = author
        self.files = []
        self.open_files()

    def open_files(self):
        filenames = os.listdir('texts/' + self.author)
        for filename in filenames:
            f = open('texts/' + self.author + '/' + filename)
            self.files.append(f)
        return filenames