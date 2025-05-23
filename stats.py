def get_num_words(book): 
    words = book.split()
    return len(words)

def get_letters(book):
    character_count = {}
    words = book.split()
    character_count[" "] = len(words) -1

    for word in words:
        letters = list(word)
        for letter in letters:
            letter = letter.lower()
            if letter in character_count:
                character_count[letter] += 1
            else: 
                character_count[letter] = 1
            
    return character_count


def dict_sort(letter_count):
    count = 0
    dict_list = []
    for i in letter_count:
        count += 1
        print(i)
        print(count)

    return
