"""
Find a candidate that occurs more number of times using Moore's element
    To find candidate, initialize maj_index = 0 and count = 1
    loop through index i from 1 till length of array
        check for element at index i is same as maj_index
            increment count
        else
            decrement count
        if count is 0
            re assign maj_index to current index i
            re assign count to 1
    Finally the element at majority index is the candidate
Check the found candidate is Majority element or not
Time complexity is O(N) and Space complexity O(1)
"""


def find_candidate(array):
    maj_index = 0
    count = 1
    for i in range(1, len(array)):
        if array[i] == array[maj_index]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return array[maj_index]


def isMajority(array):
    candidate = find_candidate(array)
    count = 0
    for i in range(len(array)):
        if array[i] == candidate:
            count += 1
    if count == ((len(array) // 2) + 1):
        return 1
    else:
        return 0


if __name__ == '__main__':
    array_in = [3, 3, 4, 2, 4, 4, 2, 4]
    ele = isMajority(array_in)
    print(ele)
