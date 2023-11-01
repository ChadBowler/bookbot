import re

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(get_char_count(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_word_count(text):
    lower_words = text.lower()
    words = re.split(',| |:|;|!|@|\\n|\?|\.|"|\(|\)|-', lower_words)
    word_set = set(words)
    word_list = {}
    for word in word_set:
        word_list[word] = 0
    for word in words:
        word_list[word] += 1
    return word_list

def get_char_count(text):
    chars = list(text.lower())
    char_set = set(chars)
    char_dict = {}
    for char in char_set:
        char_dict[char] = 0
    for char in chars:
        char_dict[char] += 1
    return char_dict



main()