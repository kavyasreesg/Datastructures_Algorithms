#Reversing array using 2 pointer index approach (start, end)
#swapping start and end index's elements
#increment start and decrement end
#This wayy we use O(1) space complexity and O(n) time complexity
arr = [1, 2, 3, 4, 5]
start = 0
end = len(arr)-1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print(arr)