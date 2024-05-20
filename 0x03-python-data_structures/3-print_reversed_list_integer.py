def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    for i in range(length, 0, -1):
        print(i)


my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)