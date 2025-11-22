import sys
from stats import word_counter, character_counter, dict_sorter

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])
        num_words = word_counter(book)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for dictionary in dict_sorter(character_counter(book)):
            print(dictionary["char"] + ": " + str(dictionary["num"]))
        print("============= END ===============")

main()