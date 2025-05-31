from stats import num_words
from stats import chars
from stats import report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_words = num_words(book_text)
    book_chars = chars(book_text)
    book_report = report(book_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_words} total words")
    print("--------- Character Count -------")
    for entry in book_report:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()