def search_replace(my_list, search, replace):
    length = len(my_list) - 1
    for i in range(length + 1):
        if my_list[i] == search:
            my_list[i] = replace
    return my_list
