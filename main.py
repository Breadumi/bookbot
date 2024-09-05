
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    num_chars, char_dict = character_count_case_insens(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    print_statistics(char_dict)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    words = text.split()
    return len(words)

def character_count_case_insens(text):
    characters = {}
    small_text = text.lower()
    for char in small_text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    print(characters)
    
    total_chars = 0
    for key in characters:
        total_chars += characters[key]
    
    return total_chars, characters

def print_statistics(chars):
    # chars is a dictionary
    # convert chars to a list of dictionaries
    list_of_dicts = expand(chars)
    list_of_dicts.sort(reverse=True, key=sort_on)

    for dict in list_of_dicts:
        char = dict["char"]
        val = dict["count"]
        if char.isalpha():
            print(f"The '{char}' character was found {val} times")
    

def sort_on(dict):
    return dict["count"]

def expand(chars):
    full_list = []
    for key in chars:
        full_list.append({"char" : key, "count" : chars[key]})
    return full_list

main()