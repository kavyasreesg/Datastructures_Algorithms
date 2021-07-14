arr = [0, 4, 3, 2, 7, 8, 2, 3, 1]
for i in range(len(arr)):
    x = arr[i] % len(arr)
    arr[x] = arr[x] + len(arr)
for i in range(len(arr)):
    if arr[i] >= 2 * len(arr):
        print(i)