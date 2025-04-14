def get_book_text(filepath):
    with open(filepath, 'r', encoding="utf-8") as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    num_words = len(words)

    return num_words


def main():
    book = f"books/frankenstein.txt"
    text = get_book_text(book)
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document")


main()
