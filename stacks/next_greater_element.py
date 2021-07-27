"""
- Given an array of elements, need to print the next
    greater element
- Use stack, add the first element to stack
- for ele in array from 1 to length
        next = -1
        pop element(pop_ele) from stack
        if pop_ele is less than array[ele]
            print pop_ele and next as array[ele]
            push array[ele] to stack
        else
            push array[ele] to stack
- for remaining elements in stack
    print -1 as next
Time Complexity is O(N) and space complexity is O(N)
"""


def next_greater_element(array):
    stack = [array[0]]
    for i in range(1, len(array)):
        next = array[i]
        element = stack.pop()
        while element < next:
            print("Next of {} is {}".format(element, next))
            if len(stack) == 0:
                break
            element = stack.pop()
        if element > next:
            stack.append(element)
        stack.append(next)

    for ele in stack:
        print("next of {} is -1".format(ele))


next_greater_element([1, 0, 2, 7, 4, 3, 11])
