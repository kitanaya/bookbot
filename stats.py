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


# def sort_on(dict):
#     return dict["num"]

def get_key_value(chars):
    sorted_list = []
    for char in chars:
        new_dict = {"char": char, "count": chars[char]}
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=lambda x: x["count"])
    return sorted_list
