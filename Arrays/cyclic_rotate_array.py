arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
d = 2
for i in range(d):
    temp = arr[n-1]
    j = n-1
    while j > 0:
        arr[j] = arr[j-1]
        j = j-1
    arr[0] = temp
print(arr)


#Time complexity O(n*d)
#space complexity O(1)