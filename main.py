import re

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text, book_path)

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
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    sorted_chars = sorted(chars.items(), key=lambda x:x[1], reverse=True)
    char_dict = dict(sorted_chars)
    return char_dict

def print_report(text, path):
    char_dict = get_char_count(text)
    print(f"--- Begin report of {path} ---\n")
    print(f"{get_number_of_words(text)} words found in the document\n")
    for char in char_dict:
        print(f"The '{char}' character was found {char_dict[char]} times\n")
    print("--- End Report ---")


main()