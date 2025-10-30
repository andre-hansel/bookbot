
def get_num_words(text):
    word_split = text.split()
    num_words = len(word_split)
    return num_words

def char_count(text):
    text = text.lower()
    char_counts_dict = {}
    for char in text:
        if char in char_counts_dict:
            char_counts_dict[char] += 1
        else:
            char_counts_dict[char] = 1
    return char_counts_dict

def dict_sort(dict):
    dict_list = []
    new_dict = {}
    for d in dict:
        new_dict = {"char": d, "num": dict[d]}
        dict_list.append(new_dict)
    def dict_helper(one_entry):
        return one_entry["num"]
    dict_list.sort(key=dict_helper,reverse=True)
    return dict_list