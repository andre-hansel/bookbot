from stats import get_num_words
from stats import char_count
from stats import dict_sort
import sys


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_counts_dict = char_count(text)
    dict_list = dict_sort(char_counts_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    for item in dict_list:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print(sys.argv)
main()