def word_count(book_text):
    return len(book_text.split())

def char_count(book_text):
    dict = {}
    for char in book_text:
        char_low = char.lower()
        if char_low in dict:
            dict[char_low] = dict[char_low] + 1
        else:
            dict[char_low] = 1
    return dict

def sort_on(items):
    return items["num"]

def sort_dict(char_dict):
    sorted_list = []
    for k in char_dict:
        if k.isalpha():
            sorted_list.append({"char": k, "num": char_dict[k]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
