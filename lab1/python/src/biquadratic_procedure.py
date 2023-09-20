import sys
import math

Testing: bool


def get_from_stdin() -> list:
    while True:
        try:
            a, b, c = map(float, input("enter coefficients a, b and c: ").split())
        except:
            print("incorrect input, you must provide 3 numbers: ")
            continue
        else:
            break

    return [a, b, c]




def get_from_cmdln(cli_args: list) -> list:
    return [cli_args[1], cli_args[2], cli_args[3]]




def get_coeffs(cli_args: list) -> list:
    a, b, c = None, None, None

    if (len(cli_args) == 4):
        try:
            a, b, c = map(float, get_from_cmdln(cli_args))
        except:
            print("incorrect arguments provided. reading from stdin.")
            return get_from_stdin()
        else:
            return [a, b, c]


    print("incorrect or no arguments provided, reading from stdin.")

    return get_from_stdin()




def try_get_pmroot(expr: float) -> list:
    if (expr < 0):
        return [None, None]

    else:
        return [-math.sqrt(expr), math.sqrt(expr)]




def solve(cli_args: list) -> set:

    if (not Testing):
        a, b, c = get_coeffs(cli_args)
    else:
        a, b, c = map(float, cli_args)


    answer = set()

    if (a == 0):

        if (b == 0 and c == 0): 
            return {math.inf}

        elif (b == 0 and c != 0): 
            return set()

        elif (b != 0):
            x_1, x_2 = try_get_pmroot((-c)/b)
            return {x_1, x_2}

    else:
        discr = b**2 - 4 * a * c

        if (discr < 0):
            return set()

        elif (discr == 0):
            x_1, x_2 = try_get_pmroot((-b) / (2 * a))
            return {sol for sol in {x_1, x_2} if sol != None}

        else:
            discr_root_1, discr_root_2 = try_get_pmroot(discr)

            x_1, x_2 = try_get_pmroot((-b + discr_root_1) / (2 * a))
            x_3, x_4 = try_get_pmroot((-b + discr_root_2) / (2 * a))

            return {sol for sol in {x_1, x_2, x_3, x_4} if sol != None}

    return answer





if __name__ == "__main__":

    Testing = False

    answer_set = solve(sys.argv) 
    print(*answer_set)