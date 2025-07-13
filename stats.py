def get_word_count(book_text):
  count = 0
  words = book_text.split()
  for word in words:
    count += 1

  return count
