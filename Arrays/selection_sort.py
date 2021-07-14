#finding the minimums and placing from the beginning of the array
arr = [1, 3, 2, 6, 5]
i = 0
n = len(arr)
while i < n-1:
    min_index = i
    j = i+1
    while j < n:
        if arr[min_index] > arr[j]:
            min_index = j
        j += 1
    arr[i], arr[min_index] = arr[min_index], arr[i]
    i += 1
print(arr) 