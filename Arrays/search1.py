# Search an element in sorted and rotated array in log(N) complexity

def search(arr, n, key):
    pivot = find_pivot(arr, 0, n - 1)  # Search index where element at that index is greater than next element
    if pivot == -1:
        binary_search(arr, 0, n - 1, key)
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binary_search(arr, 0, pivot - 1, key)
    return binary_search(arr, pivot + 1, n - 1, key)


def find_pivot(ar, low, high):
    if high < low:
        return -1
    if high == low:
        return low
    mid = int((low + high) / 2)
    if mid < high and ar[mid] > ar[mid + 1]:
        return mid
    if mid > low and ar[mid] < ar[mid - 1]:
        return mid - 1
    if ar[low] >= ar[mid]:
        return find_pivot(ar, low, mid - 1)
    return find_pivot(ar, mid + 1, high)


def binary_search(inp_arr, low_ind, high_ind, element):
    if high_ind < low_ind:
        return -1
    mid = int((low_ind + high_ind) / 2)
    if inp_arr[mid] == element:
        return mid
    if element > inp_arr[mid]:
        return binary_search(inp_arr, mid + 1, high_ind, element)
    return binary_search(inp_arr, low_ind, mid - 1, element)


array_in = [3, 4, 5, 1, 2]
print(search(array_in, len(array_in), 2))

# Time complexity is O(logN) and space complexity is O(1)
