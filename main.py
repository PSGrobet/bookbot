import sys
from stats import count_words, count_chars, list_chars, sort_on, print_data

def main(book):
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    #print(get_book_text(book))
    num_words = count_words(book)
    chars = count_chars(book)
    chars_list = list_chars(chars)
    chars_list.sort(reverse=True, key=sort_on)
    print_data(chars_list, num_words, book)
    

main("frankenstein.txt")