def element_at(my_list, idx):
    size_of_list = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > size_of_list:
        return None
    else:
        for i in my_list:
            if i == my_list[idx]:
                return i


my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))