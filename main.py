def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
    return char_count

def sort_on(dict):
    return dict["num"]

def report(text):
    char_counts = count_char(text)
    char_list = [{"char": char, "num": num} for char, num in char_counts.items()]
    char_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")

    for char_dict in char_list:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"The '{char}' character was found {num} times")

    print(f"--- End report ---")

main()