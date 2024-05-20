def print_sorted_dictionary(a_dictionary):
    dic_lists = []
    for key in a_dictionary.keys():
        dic_lists.append(key)
    sorted_keys = sorted(dic_lists)
    for key in sorted_keys:
        print(f"{key} : {a_dictionary[key]}")

    return a_dictionary