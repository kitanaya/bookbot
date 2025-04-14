from stats import get_word_count
from stats import get_char_count
from stats import get_key_value
from pathlib import Path


def get_book_text(filepath):
    path = Path(filepath)
    if not path.exists():
        print(f"Error: File {filepath} does not exist!")
        return ""
    with open(filepath, 'r', encoding="utf-8") as f:
        return f.read()


def main():
    book = f"books/frankenstein.txt"
    text = get_book_text(book)
    num_words = get_word_count(text)
    num_chars = get_char_count(text)
    sorted_list = get_key_value(num_chars)
    
    header = f"""============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------"""
    footer = f"============= END ==============="

    print(header)
    for letter in sorted_list:
        if letter["char"].isalpha():
            # Pad each count number to be consistently aligned
            # print(f'{letter["char"]}: {str(letter["count"]).rjust(6)}')
            print(f'{letter["char"]}: {letter["count"]}')
    print(footer)


main()
