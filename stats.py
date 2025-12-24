def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(path):
    book_text = get_book_text(path)     
    words = book_text.split()
    word_count = len(words)
    print(f"Found {word_count} total words")

def get_num_char(path):
    char_count_dict = {}
    text = get_book_text(path)
    text = text.casefold()

    for char in text:
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1

    return char_count_dict

def sort_on(dict_item):
    return dict_item["num"]   

def sort_chars(path):
    char_dict = get_num_char(path)
    char_list = []
   
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list


    
