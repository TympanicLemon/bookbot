def get_word_count(book_text):
  count = 0
  words = book_text.split()
  for word in words:
    count += 1

  return count

def get_letter_counts(book_text):
  letter_counts = {
      'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
      'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
      'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }

  words = book_text.split()
  for word in words:
    word = word.lower()
    for char in word:
      if char in letter_counts:
        letter_counts[char] += 1

  return letter_counts

def sort_counts(counts):
  dict_list = []
  for key in counts:
    dict_list.append({ "char": key, "count": counts[key]})

  dict_list.sort(reverse=True, key=lambda item: item["count"])
  return dict_list
