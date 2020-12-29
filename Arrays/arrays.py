import array

# creating array using array module
arr = array.array('i', [1, 1, 3, 1, 2, 3])

# Performing append() operation
arr.append(4)  # [1, 1, 3, 1, 2, 3, 4]

# performing insert() operation
arr.insert(2, 7)  # [1, 1, 3, 7, 1, 2, 3, 4]

# Performing pop() operation
arr.pop(1)  # [1, 3, 7, 1, 2, 3, 4]

# Performing remove() operation
arr.remove(1)  # [3, 7, 1, 2, 3, 4]

# Performing index() operation
print("The index of first occurrence of element 3 is {}".format(arr.index(3)))

# Performing reverse() operation
arr.reverse()  # [4, 3, 2, 1, 3, 7]

# Printing the transformed array
print("The final array after performing above operations is {} " + format(arr))
