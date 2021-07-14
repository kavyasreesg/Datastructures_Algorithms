#check each element with all the elements other than that index
arr = [2, 1, 4, 3, 6, 5, 0]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)
