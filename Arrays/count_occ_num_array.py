#frequency of x in array
#Time complexity O(n)
arr = [0, 5, 5, 5, 4]
count = 0
x = 5
for i in range(len(arr)):
    if arr[i] == x:
        count += 1
print(count)