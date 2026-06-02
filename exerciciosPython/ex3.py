# Group a list of strings by length and return as a dict
def group_words(words):
    sizes_dict = {}
    word_list = []
    for word in words:
        length = len(word)
        sizes_dict[length] = word


    return word_list

print(group_words(["sol", "lua", "beijo"]))