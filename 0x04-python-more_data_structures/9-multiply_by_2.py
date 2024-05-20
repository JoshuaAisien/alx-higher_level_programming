def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    new_list = list(new_dictionary)
    print(new_list)

    for i in new_list:
        new_dictionary[i] *= 2
    return new_dictionary


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
multiply_by_2(a_dictionary)