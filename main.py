file_contents = ""
with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count

def print_report():
    print("--- Begin report of books/frankenstein.txt ---")
    words = print(count_words(file_contents))
    print(f"{words} words found in the document")
    char_count = count_chars(file_contents)
    for key in char_count:
        if key.isalpha():
            print(f"The '{key}' character was found {char_count[key]} times")

print_report()
