from lab1.constants import CALCULATION_ACCURACY


def get_solution_via_gauss_method(a: list, b: list) -> list:
    n = len(a)

    for i in range(n):
        if a[i][i] == 0:
            for j in range(i + 1, n):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    b[i], b[j] = b[j], b[i]
                    break
        for j in range(i + 1, n):
            coeff = -a[j][i] / a[i][i]
            a[j] = [round(a[j][k] + coeff * a[i][k], CALCULATION_ACCURACY) for k in range(n)]
            b[j] += coeff * b[i]

    print("\nПреобразованная матрица:")
    col_width = CALCULATION_ACCURACY + 4
    for i in range(len(a)):
        for val in a[i]:
            print(f'{val:>{col_width}.{CALCULATION_ACCURACY}f}', end=' ')
        print(f'{b[i]:>{col_width}.{CALCULATION_ACCURACY}f}', end='\n')

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= a[i][j] * x[j]
        x[i] = round(x[i] / a[i][i], CALCULATION_ACCURACY)
    return x
