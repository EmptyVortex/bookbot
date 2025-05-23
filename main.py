from stats import get_num_words
from stats import get_letters
from stats import dict_sort

def main(): 
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book)
    letter_count = get_letters(book)
    letter_list = dict_sort(letter_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for i in letter_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as book:
        return book.read()
        


main()