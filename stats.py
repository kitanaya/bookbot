def get_word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_char_count(text):
    num_chars = {}
    for char in text.lower():
        if char not in num_chars:
            num_chars[char] = 1
        else:
            num_chars[char] += 1
    return num_chars