def replace_in_list(my_list, idx, element):
    """
    replace elements in list
    """

    size_of_mylist = len(my_list) - 1
    if idx < 0 :
        return my_list
    elif idx > size_of_mylist:
        return my_list
    else:
        my_list[idx] =  new_element
        return my_list


my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)