def uniq_add(my_list=[]):
    value = 0
    uniq_numbers = set(my_list)
    for i in uniq_numbers:
        value = value + i
    return value
