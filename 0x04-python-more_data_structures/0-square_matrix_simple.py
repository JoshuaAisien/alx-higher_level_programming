def square_matrix_simple(matrix=[]):
    matrix_2 = []
    for row in matrix:
        matrix_1 = []
        for i in row:
            value = i * i
            matrix_1.append(value)
        matrix_2.append(matrix_1)
    return matrix_2
