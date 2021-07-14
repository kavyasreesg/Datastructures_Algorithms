arr = [1,2,3,4,5,6]
d=2
n=len(arr)
for i in range(d):
    temp = arr[0]
    for j in range(n-1):
        arr[j] = arr[j+1]
    arr[n-1]=temp
print(arr)

#Time complexity O(n*d)
#space complexity O(1)