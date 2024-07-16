def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    char_count = get_word_amount(text)
    sorted_chars = convert_dict(char_count)  # Correctly calling convert_dict with char_count
    print_report(sorted_chars)  # Making sure to print the sorted report


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_amount(text):
    lowercase = text.lower()
    chars = {}
    for char in lowercase:
        if char.isalpha():  # Consider only alphabetic characters
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars


def convert_dict(char_count):
    chars = []
    for char, num in char_count.items():
        chars.append({"char": char, "num": num})
    
    def sort_on(item):
        return item["num"]

    chars.sort(reverse=True, key=sort_on)  # Sort the list in descending order
    return chars


def print_report(sorted_chars):
    print("--- Begin report of books/frankenstein.txt ---")
    for item in sorted_chars:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


main()