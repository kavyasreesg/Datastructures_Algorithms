def rotate_once(array_one, n):
    temp = array_one[0]
    for i in range(1, n):
        array_one[i - 1] = array_one[i]
    array_one[n - 1] = temp


def rotate_array(arr, n, d):
    for i in range(d):
        rotate_once(arr, n)
    return arr


if __name__ == "__main__":
    array_in = [1, 2, 3, 4, 5]
    print(rotate_array(array_in, 5, 2))

# Time complexity is O(n*d) and Space complexity is O(1)
