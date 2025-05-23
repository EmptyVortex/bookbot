count = 0

def get_book_text(path):
    with open(path) as book:
        return book.read()
        

def main(): 
    count = 0
    book = get_book_text("./books/frankenstein.txt")
    words = book.split()
    for word in words:
        count += 1
    print(f"{count} words found in the document")

main()