import sys
from stats import *

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        text = get_book_text(path)
        word_count = count_words(text)
        char_counts = count_characters(text)
        sorted_chars = sorted_dict(char_counts)
    
        # formatted
        print("\n+++ BOOK BOT +++")
        print(f"Analysis of book found at {path}...\n")
        print("Word Count:")
        print(f"Found {word_count} total words\n")
        print("Character count:")

        for char_dict in sorted_chars:
            char = char_dict["char"]
            if char.isalpha():    # only alphabetical
                print(f"{char}: {char_dict['num']}")
    

main()