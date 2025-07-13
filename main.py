def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents

def get_word_count(book_text):
  count = 0
  words = book_text.split()
  for word in words:
    count += 1

  return count


def main():
  book_text = get_book_text("books/frankenstein.txt")
  count = get_word_count(book_text)
  print(f"{count} words found in the document")

main()
