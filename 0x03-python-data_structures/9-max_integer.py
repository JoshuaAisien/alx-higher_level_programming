def max_integer(my_list=[]):
    if len(my_list) == 0:
        return  None
    else:
        new_list = my_list[0]
        length = len(my_list) -1
        for i in range(length):
            if my_list[i] > new_list:
                new_list = my_list[i]

        return new_list


my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))