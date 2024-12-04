def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count(text):
    words = text.split()
    return len(words)
    

def count_chars(text):
    report = {}
    chars = list(text.lower())
    # print(chars)
    for char in chars:
        if char in report:
            report[char] += 1
        else:
            report[char] = 1
    return report
    
def sort_on(d):
    return d["num"]

def convert_to_sorted_list(d):
    sorted_list = []
    for char in d:
        sorted_list.append({"char": char, "num": d[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


if __name__ == '__main__':
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count(text)
    chars = count_chars(text)
    sorted = convert_to_sorted_list(chars)
    print(f"--- Begin report of {book_path} ---")
    print(f"There are {words} words found in the document")
    for item in sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End Report ---")
