def word_counter(text):
    return len(text.split())

def character_counter(text):
    char_dict = {}
    for character in text:
        if character.lower() not in char_dict:
            char_dict[character.lower()] = 1
        else:
            char_dict[character.lower()] += 1
    return char_dict

def sort_helper(items):
    return items["num"]

def dict_sorter(dictionary):
    dict_list = []
    for letter, count in dictionary.items():
        if letter.isalpha():
            count_dict = {}
            count_dict["char"] = letter
            count_dict["num"] = count
            dict_list.append(count_dict)
    dict_list.sort(reverse=True, key=sort_helper)
    return dict_list
