from stats import get_num_words
from stats import get_letters
from stats import dict_sort
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main(): 
    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)
    letter_count = get_letters(book)
    letter_list = dict_sort(letter_count)
    print_report(num_words, letter_list)
    
   

def get_book_text(path):
    with open(path) as book:
        return book.read()
        
def print_report(num_words, letter_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for i in letter_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")



main()