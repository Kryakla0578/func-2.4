def get_matrix(n, m, value):
    matrix = []
    for i in range (n):
        matrix.append([])
        for j in range (m):
            matrix[i].append(value)
    print(matrix)
    return  matrix

result_1 = get_matrix(2,2,10)
result_2 = get_matrix(3,5,42)
result_3 = get_matrix(4,2,13)