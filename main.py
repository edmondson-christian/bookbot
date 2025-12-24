from stats import get_book_text, get_num_words, get_num_char, sort_chars
import sys 

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

get_book_text(path)

get_num_words(path)

sorted_chars = sort_chars(path)
for item in sorted_chars:
    print(f"{item['char']}: {item['num']}")