def count_words(book_text):
    tmp = book_text.split()
    return len(tmp)

def count_letters(book_text):
    chars = dict()
    for char in book_text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(items):
    return items["num"]

def fuck_sort(letter_dict):
    why = list()
    for letter in letter_dict:
        why.append({"char": letter, "num": letter_dict[letter]})
    why.sort(reverse=True, key=sort_on)
    return why