#sorting happens by repeatedly comparing the adjacent elements
arr = [1,11,9,2,10,15]
for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)