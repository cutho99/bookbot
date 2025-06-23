def get_num_words(s):
    num_words = len(s.split())
    return num_words


#function to store char & count in a dict
def char_count(t):
    raw_input = t.lower()
    word_list = raw_input.split()
    char_dict = {}
    for word in word_list:
        for c in word:
            if c not in char_dict:
                char_dict[c] = 1
            else:
                char_dict[c] += 1
    return char_dict


#Create a list w input from the raw dict, filter only alpha char, and order it based on count 
def show_order_char_count(d):
    main_list = []
    for key in d:
        if key.isalpha():
            main_list.append({"char": key , "num":d[key]})
    
    def sort_on(items):
        return items["num"]

    main_list.sort(reverse=True, key=sort_on)               #.sort method calls the "sort_on" function for each item 
    return main_list
