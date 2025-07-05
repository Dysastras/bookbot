
import sys
from stats import get_num_words, count_characters, sort_characters


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = count_characters(book_text)
    sorted_chars = sort_characters(char_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()


