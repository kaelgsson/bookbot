from stats import get_num_words, get_num_chars, sort_it
import sys

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main(book_path) -> None:
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    sorted_dicts = sort_it(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dicts:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        sys.exit(main(sys.argv[1]))