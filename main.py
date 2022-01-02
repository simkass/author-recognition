import math
from author_recognition.author_collection import AuthorCollection
authors = ['Agatha Christie', 'Arthur Conan Doyle', 'Charles Dickens', 'Jane Austen',
           'Mark Twain', 'Oscar Wilde', 'William Shakespeare', 'William Somerset']

from author_recognition.utils import bcolors

def evaluate_similarity(author1_collection, author2_collection):
    common_words = [word for word in author2_collection.dictionary.keys() if word in author1_collection.dictionary.keys()]

    similarity, common_words_total_a1, common_words_total_a2 = 0, 0, 0
    for word in common_words:
        common_words_total_a1 += author1_collection.dictionary[word].get_count()
        common_words_total_a2 += author2_collection.dictionary[word].get_count()

    for word in common_words:
        similarity += pow((author2_collection.dictionary[word].get_count() / common_words_total_a2) - (
            author1_collection.dictionary[word].get_count() / common_words_total_a1), 2)

    return round(0.1 / math.sqrt(similarity), 2)


def identify_author(mystery_author):
    similarities = {}

    mystery_author_collection = AuthorCollection(mystery_author, test=True)

    for author in authors:
        author_collection = AuthorCollection(author)
        sim = evaluate_similarity(mystery_author_collection, author_collection)
        similarities[author] = sim
        print(bcolors.ENDC + 'Similarity between mystery author and ' + author + ': ' + str(sim))

    identification = max(similarities, key=similarities.get)
    if identification == mystery_author:
        print(bcolors.OKGREEN + 'Mystery author successfully identified as ' + identification)
    else:
        print(bcolors.FAIL + 'Mystery author wrongly identified as ' + identification)
        print(bcolors.WARNING + 'Mystery author is actually ' + mystery_author)


def main():
    for author in authors:
        print(bcolors.ENDC + '----------------------------------------------------------')
        identify_author(author)


if __name__ == '__main__':
    main()