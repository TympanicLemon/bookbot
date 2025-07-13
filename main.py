import sys
from stats import get_letter_counts, get_word_count, sort_counts

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]
  book_text = get_book_text(book_path)

  count = get_word_count(book_text)
  letter_counts = get_letter_counts(book_text)
  sorted_counts = sort_counts(letter_counts)
  header = f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------"""

  print(header)
  print(f"Found {count} total words")
  print("--------- Character Count -------")
  for item in sorted_counts:
    char = item["char"]
    count = item["count"]
    print(f"{char}: {count}")
  print("============= END ===============")

main()
