def add_tuple(tuple_a=(), tuple_b=()):
    # if tuple are smaller than 2 pad with zero's
    tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1,)))
print(add_tuple(tuple_a, ()))
