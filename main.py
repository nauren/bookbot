import sys
from stats import count_words, count_letters, fuck_sort


def get_book_text(file_path):
    with open(file_path) as p:
        retval = p.read()
    return retval



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    num_words = count_words(book)
    letters_dict = count_letters(book)
    fucky_list = fuck_sort(letters_dict)
    
    print(f'''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
''')
    for d in fucky_list:
        print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")

main()

