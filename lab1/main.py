import copy
import time

from memory_profiler import profile

from lab1.determinant import *
from lab1.gauss import *
from lab1.input_manager import *
from lab1.residual import *
from lab1.utils import *


@profile()
def main():
    start_time = time.time_ns()

    matrix = get_matrix_from_user_input()

    main_matrix = get_main_matrix(matrix)
    free_member_column = get_free_member_column(matrix)

    determinant = get_determinant(copy.deepcopy(main_matrix))
    print("\nДетерминант:", determinant)
    if determinant == 0:
        print("Т.к. детерминант равен 0, решений нет!")
        return

    solution = get_solution_via_gauss_method(copy.deepcopy(main_matrix),
                                             copy.deepcopy(free_member_column))

    print_solution(solution)
    print("\nНевязка:", get_residual(main_matrix[:], free_member_column[:], solution))
    print("\nВремя работы программы:", round(time.time_ns() - start_time), "нс.\n\n")


if __name__ == '__main__':
    main()
