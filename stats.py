def word_count(book: str ) -> int:
    num_words = book.split()
    return len(num_words)

def total_char(book: str) -> dict[str, int]:
    total_list = {}
    for i in book:
        i = i.lower()
        if i not in total_list:
            total_list[i] = 1
        else:
            total_list[i] += 1
    return total_list

def sort_on(char_list: tuple[str, int]) -> int:
    return char_list[1]

def char_dict_to_sorted_list(total_list):
    char_list = []
    for i in total_list:
        count = total_list[i]
        char_list.append((i, count))
    sorted_list = sorted(char_list, reverse = True, key = sort_on)
    return sorted_list
