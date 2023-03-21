def get_main_matrix(matrix: list) -> list:
    main_matrix = []
    for i in range(len(matrix)):
        main_matrix.append(matrix[i][:-1])
    return main_matrix


def get_free_member_column(matrix: list) -> list:
    free_member_column = []
    for i in range(len(matrix)):
        free_member_column.append(matrix[i][-1])
    return free_member_column


def print_solution(solution: list):
    print("\nРешение:")
    for i in range(len(solution)):
        print(f"X{i + 1}={solution[i]}")