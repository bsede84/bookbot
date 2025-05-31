def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import num_words

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_words = num_words(book_text)

    print(f"{book_words} words found in the document")

main()