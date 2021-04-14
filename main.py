from author_recognition.author_dictionary import AuthorDictionary

def main():
    authors = ['Agatha Christie']
    author_dict = AuthorDictionary('Agatha Christie')
    print(author_dict.files)


if __name__ == '__main__':
    main()
