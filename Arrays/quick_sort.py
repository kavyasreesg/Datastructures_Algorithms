def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
        arr_lower = []
        arr_higher = []
        for ele in arr:
            if ele <= pivot:
                arr_lower.append(ele)
            else:
                arr_higher.append(ele)
        return quick_sort(arr_lower) + [pivot] + quick_sort(arr_higher)
        
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(quick_sort(arr))

#Way to move all negative elements to one part and positive to right end
j = 0
for i in range(len(arr)):
    if arr[i] < 0:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        j += 1
print(arr)