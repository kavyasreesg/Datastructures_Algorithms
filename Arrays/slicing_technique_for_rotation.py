arr = [1, 2, 3, 4, 5]
d = 2  # Rotate twice

# Anti Clockwise
arr[:] = arr[d:len(arr)] + arr[0:d] # O(N) Time Complexity
print(arr)
# clockwise
arr = [1, 2, 3, 4, 5]
arr[:] = arr[len(arr) - d:len(arr)] + arr[0: len(arr) - d]
print(arr)
