array = [1,2,3,4,5,6,7,8,9]
d = 5
n = len(array)
temp = []
for i in range(d):
    temp.append(array[i])
    
for i in range(n-d):
    array[i] = array[i+d]

for j in range(len(temp)):
    array[n-1-j] = temp[d-1-j]
print(array)

#Time complexity O(n)
#space complexity O(d)