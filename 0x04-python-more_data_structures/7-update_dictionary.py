def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        # update the value of the existing key
        a_dictionary[key] = value
    else:
        # if not found replace the value with
        a_dictionary[key] = value
    return a_dictionary
