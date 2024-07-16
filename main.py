def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_count = get_word_amount(text)
    print(char_count)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_word_amount(text):
    lowercase = text.lower()
    chars = {}
    for char in lowercase:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars
    


main()