from stats import get_word_count

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents

def main():
  book_text = get_book_text("books/frankenstein.txt")
  count = get_word_count(book_text)
  print(f"{count} words found in the document")

main()
