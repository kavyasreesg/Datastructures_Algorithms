"""
if array[i] > array[j] and i < j then inversion count increments
This can be made possible by merge sort while merging
Time complexity is O(nlogn) and space complexity is O(n)
"""


def merge_sort(array):
    Inversion_count = 0
    if len(array) > 1:
        mid = len(array) // 2
        L = array[:mid]
        R = array[mid:]
        Inversion_count = merge_sort(L)
        Inversion_count += merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
                Inversion_count += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    return Inversion_count


arr = [10, 1, 4, 3, 2, 11, 9]
count = merge_sort(arr)
print(arr, count)
