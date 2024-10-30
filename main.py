from tkinter.font import names


def word_count(text):
    count = 0
    for word in text.split():
        count += 1

    return count

def print_char_count(text):
    letters = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,
        "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
        "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
        "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
        "y": 0, "z": 0
    }

    for word in text:
        for char in word:
            if char.isalpha():
                letters[char.lower()] += 1

    for item in letters:
        print(item, ":", letters[item])


def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt", 'r') as file:
        contents = file.read()
        count = word_count(contents)
        print(f"{count} words found in the document.")
        print_char_count(contents)


if __name__ == "__main__":
    main()
