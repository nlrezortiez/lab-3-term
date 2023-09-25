import sys
import math

Testing: bool


def try_get_pmroot(expr: float) -> list:
    if (expr < 0):
        return [None, None]

    else:
        return [-math.sqrt(expr), math.sqrt(expr)]


class Solution:
    solution_set: set = set()
    solution_amount: int = 0

    def __init__(self):
        self.solution_set = set()
        self.solution_amount = 0

    def add_solution(self, solution):
        self.solution_set.add(solution)
        self.solution_amount += 1

    def check_if_inf(self):
        for sol in self.solution_set:
            if (sol == math.inf):
                self.solution_amount = int(math.inf)


class Equation:
    a: float = math.nan
    b: float = math.nan
    c: float = math.nan

    solution: Solution = Solution()

    def __init__(self, a = 0.0, b = 0.0, c = 0.0):
        self.solution = Solution()
        self.a = a
        self.b = b
        self.c = c



    def __get_from_stdin(self):
        while True:
            try:
                a, b, c = map(float, input("enter coefficients a, b and c: ").split())
            except ValueError:
                print("incorrect input, you must provide 3 numbers: ")
                continue
            else:
                break

        self.a = a
        self.b = b
        self.c = c

    def __get_from_cmdln(self, cli_args: list):
        if not Testing:
            self.a = float(cli_args[1])
            self.b = float(cli_args[2])
            self.c = float(cli_args[3])
        else:
            self.a = float(cli_args[0])
            self.b = float(cli_args[1])
            self.c = float(cli_args[2])

    def get_coeffs(self, cli_args: list):
        try:
            self.__get_from_cmdln(cli_args)
        except ValueError:
            print("incorrect arguments provided. reading from stdin.")
            self.__get_from_stdin()

    def solve(self):
        if (self.a == 0):

            if (self.b == 0 and self.c == 0):
                self.solution.add_solution(math.inf)
                return

            elif (self.b == 0 and self.c != 0):
                return

            elif (self.b != 0):
                x_1, x_2 = try_get_pmroot((-self.c)/self.b)
                self.solution.add_solution(x_1)
                self.solution.add_solution(x_2)

        else:

            discr = self.b**2 - 4 * self.a * self.c

            if (discr < 0):
                return

            elif (discr == 0):
                x_1, x_2 = try_get_pmroot((-self.b) / (2 * self.a))
                if (x_1 is not None):
                    self.solution.add_solution(x_1)
                if (x_2 is not None):
                    self.solution.add_solution(x_2)

            else:
                discr_root_1, discr_root_2 = try_get_pmroot(discr)

                x_1, x_2 = try_get_pmroot((-self.b + discr_root_1) / (2 * self.a))
                x_3, x_4 = try_get_pmroot((-self.b + discr_root_2) / (2 * self.a))

                for i in {x_1, x_2, x_3, x_4}:
                    if i is not None:
                        self.solution.add_solution(i)

        self.solution.check_if_inf()

    def print_solution(self):
        if (self.solution.solution_amount == 0):
            print("no solutions")
        elif (self.solution.solution_amount == math.nan):
            print("inf amount of solutions")
        else:
            print(*self.solution.solution_set)


if __name__ == "__main__":
    Testing = False

    equation: Equation = Equation()

    equation.get_coeffs(sys.argv)
    equation.solve()
    equation.print_solution()
