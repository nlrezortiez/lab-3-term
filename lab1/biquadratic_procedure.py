import sys
import math

def solve(arg_list: list):
    if len(arg_list) != 1:
        a_coeff, b_coeff, c_coeff = float(arg_list[1]), float(arg_list[2]), float(arg_list[3])
    else:
        a_coeff, b_coeff, c_coeff = map(float, input().split())

    if (a_coeff == 0):
        if (b_coeff == 0):
            if (c_coeff == 0):
                print("inf solutions")
                return [None] * 4
            else:
                print("no solutions")
                return [None] * 4
        else:
            x_1 = math.sqrt(-c_coeff / b_coeff)
            x_2 = -math.sqrt(-c_coeff / b_coeff)
            return [x_1, x_2]
    else:
        discr = b_coeff ** 2 - 4 * a_coeff * c_coeff
        if (discr < 0): return [None] * 4
        elif (discr == 0): 
            x_1 = math.sqrt(-b_coeff / 2 * a_coeff)
            x_2 = -math.sqrt(-b_coeff / 2 * a_coeff)
        else:
            under_root_1 = (-b_coeff + math.sqrt(discr)) / 2 * a_coeff
            under_root_2 = (-b_coeff - math.sqrt(discr)) / 2 * a_coeff
            x_1, x_2, x_3, x_4 = None, None, None, None 
            if (under_root_1 >= 0):
                x_1 = math.sqrt(under_root_1)
                x_2 = -x_1
            if (under_root_2 >= 0):
                x_3 = math.sqrt(under_root_2)
                x_4 = -x_3

            return [x_1, x_2, x_3, x_4]
        




if __name__ == "__main__":
    print(" ".join(sys.argv))
    answer_list = solve(sys.argv) 
    print(*answer_list)
