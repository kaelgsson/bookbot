def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words_in_text(text):
    number_of_words = len(text.split())
    return number_of_words

def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words_in_text(book_text)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()