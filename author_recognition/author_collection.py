import os

from author_recognition import utils
from author_recognition.word import Word


class AuthorCollection:
    def __init__(self, author, test=False):
        self.subfolder = 'test/' if test else 'train/'
        self.author = author
        self.files = []
        self.dictionary = {}
        self.open_files()
        self.build_dictionary()

    def open_files(self):
        filenames = os.listdir('texts/' + self.subfolder + self.author)
        for filename in filenames:
            f = open('texts/' + self.subfolder + self.author + '/' + filename, encoding='utf8')
            self.files.append(f)

    def build_dictionary(self):
        for f in self.files:

            previous_word = None
            line = f.readline()

            while line:
                line_words = utils.format_line(line)
                for word in line_words:
                    previous_word = self.add_to_dictionary(word, previous_word)
                line = f.readline()
            f.close()

    def add_to_dictionary(self, word, previous_word):
        if word not in self.dictionary.keys():
            self.dictionary[word] = Word(word)
        else:
            self.dictionary[word].increment_count()

        if previous_word != None:
            if word not in self.dictionary[previous_word].get_following_words().keys():
                self.dictionary[previous_word].add_following_word(word)
            else:
                self.dictionary[previous_word].increment_following_word(word)
        return word
