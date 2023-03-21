def get_determinant(matrix: list) -> float:
    n = len(matrix)
    det = 1
    for i in range(n):
        max_elem = abs(matrix[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_elem:
                max_elem = abs(matrix[k][i])
                max_row = k
        if max_elem == 0:
            return 0
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            det *= -1
        det *= matrix[i][i]
        for j in range(i + 1, n):
            c = matrix[j][i] / matrix[i][i]
            for k in range(i + 1, n):
                matrix[j][k] -= c * matrix[i][k]
            matrix[j][i] = 0
    return det
