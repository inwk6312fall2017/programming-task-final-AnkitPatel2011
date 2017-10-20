def longest_word(Book1):
    with open("Book1.txt", "r") as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('Book1.txt'))


def longest_word(Book2):
    with open("Book2.txt", "r") as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('Book2.txt'))


def longest_word(Book3):
    with open("Book3.txt", "r") as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('Book3.txt'))

