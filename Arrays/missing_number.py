arr = [1,2,4,6,3,7,8]
new_arr = []
length = len(arr)+1
for i in range(length):
    new_arr.append(i+1)
for i in range(len(arr)):
    if arr[i] in new_arr:
        new_arr.remove(arr[i])
for i in new_arr:
    print(i)
#space complexity is O(N) and TC is O(N)

#optimize
length1 = len(arr)+1
sum = (length1*(length1+1))//2
sum1 = 0
for i in range(len(arr)):
    sum1 += arr[i]
print(sum-sum1)
#Time complexity is O(N) and space complexity is O(1)