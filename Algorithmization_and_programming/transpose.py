transpose_matrix = []

with open('matrix.txt', 'r', encoding='UTF-8') as f:
    matrix = f.read()
    matrix = matrix.split()
    f.seek(0)
    matrix_columns = len(f.readline().split())
    matrix_rows = len(matrix) // matrix_columns
    new_matrix = []
    column_index = 0
    # print(matrix_rows, matrix_columns, matrix)

    for i in range(matrix_columns):
        tmp = []
        index = column_index
        for k in range(matrix_rows):
            tmp.append(matrix[index])
            index += matrix_columns
        new_matrix.append(tmp)
        column_index += 1

with open('transpose_matrix.txt', 'w', encoding='UTF-8') as f:
    for i in new_matrix:
        f.write(' '.join(i) + '\n')
