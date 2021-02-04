from math import sqrt, floor


def is_perfect_square(number):
    if sqrt(number) - floor(sqrt(number)) == 0:
        return True
    return False


def nearest_perfect_number(n):

    if is_perfect_square(n):
        return

    upper = -1
    lower = -1
    n1 = n + 1
    while True:
        if is_perfect_square(n1):
            upper = n1
            break
        n1 = n1 + 1

    n1 = n - 1
    while True:
        if is_perfect_square(n1):
            lower = n1
            break
        n1 = n1 - 1

    diff_1 = upper - n
    diff_2 = n - lower

    if diff_1 < diff_2:
        print(upper)
    else:
        print(lower)


nearest_perfect_number(1500)
