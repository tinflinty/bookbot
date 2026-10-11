import sys
from stats import word_count
from stats import total_char
from stats import char_dict_to_sorted_list

def get_book_text(file: str) -> str:
    with open(file) as f:
        file_contents = f.read()
    return file_contents



def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = word_count(text)
    total_characters = total_char(text)
    sorted = char_dict_to_sorted_list(total_characters)
    print_report(path, num_words ,sorted)

def print_report(path: str, word_count: int, char_count):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}")
    print(f"----------- Word Count ----------\nFound {word_count} total words")
    print("--------- Character Count -------")
    for char, count in char_count:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()
#main("books/frankenstein.txt")
