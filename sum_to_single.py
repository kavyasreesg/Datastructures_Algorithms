# Problem
# Finding sum of digits of a number until sum becomes single digit

# Time complexity : O(1)

def sum_digits_to_one_digit(number):
    if number % 9 == 0:
        return 9
    if number == 0:
        return 0
    else:
        return number % 9


if __name__ == "__main__":
    n = 1000
    print(sum_digits_to_one_digit(n))
