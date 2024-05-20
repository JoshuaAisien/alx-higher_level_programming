def number_keys(a_dictionary):
    lists_of_keys = []
    for key, value in a_dictionary.items():
        lists_of_keys.append(key)
    return len(lists_of_keys)

