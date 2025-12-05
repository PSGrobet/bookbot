def get_book_text(book):
    with open(f"{book}") as text:
        return text.read()

def count_words(book):
    return len(get_book_text(book).split())

def count_chars(book):
    book = get_book_text(book)
    counts = {}
    for c in book:
        if c.lower() in counts:
            counts[c.lower()] += 1
        else:
            counts[c.lower()] = 1
    return counts

def list_chars(dict):
    chars = []
    for key in dict:
        chars.append({"char": key, "num": dict[key]})
    return chars

def sort_on(dict):
    #pass the inner dictionaries, not the full list
    return dict["num"]

def print_data(chars, num_words, book):
    #chars.sort(key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")