from stats import get_num_words

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main() -> None:
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()