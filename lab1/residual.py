from lab1.constants import CALCULATION_ACCURACY


def get_residual(a: list, b: list, x: list) -> list:
    residual = []
    for i in range(len(b)):
        temp = 0
        for j in range(len(x)):
            temp += a[i][j] * x[j]
        residual.append(round(b[i] - temp, CALCULATION_ACCURACY))
    return residual
