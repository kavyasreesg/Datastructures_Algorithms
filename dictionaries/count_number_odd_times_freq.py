"""
Best solution is to do XOR of all the elements
The element occurring odd number of times, that element is returned
A ^ A = 0
A ^ 0 = A
Time Complexity : O(N) and Space Complexity is O(1)
"""


def odd_occ_element(array):
    res = 0
    for i in range(len(array)):
        res = res ^ array[i]
    return res


if __name__ == '__main__':
    array_in = [1, 1, 2, 2, 3, 4, 2, 5, 4, 5, 3]
    result = odd_occ_element(array_in)
    print(result)
