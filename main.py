from stats import get_num_words
from stats import get_letters
from stats import dict_sort

def main(): 
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book)
    print(f"{num_words} words found in the document")
    letter_count = get_letters(book)
    print(letter_count)
    dict_sort(letter_count)
    


def get_book_text(path):
    with open(path) as book:
        return book.read()
        


main()