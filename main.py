from stats import get_letter_counts, get_word_count

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents

def main():
  book_text = get_book_text("books/frankenstein.txt")
  count = get_word_count(book_text)
  print(f"{count} words found in the document")
  letter_counts = get_letter_counts(book_text)

  print("\nCount for number of times each letter appears in the book:")
  for char in letter_counts:
    print(f"'{char}': {letter_counts[char]}")

main()
