from stats import get_letter_counts, get_word_count, sort_counts

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents

def main():
  book = "books/frankenstein.txt"
  book_text = get_book_text(book)

  count = get_word_count(book_text)
  letter_counts = get_letter_counts(book_text)
  sorted_counts = sort_counts(letter_counts)
  header = f"""============ BOOKBOT ============
Analyzing book found at {book}...
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
