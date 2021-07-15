# class Node:
#     def __init__(self, data, next=None, down=None):
#         self.data = data
#         self.next = next
#         self.down = down
#
#
# def create_vertical_list(head, linkedlist):
#     for ele in linkedlist:
#         head = Node(ele, head)
#         print(head.data, end=' ')
#         temp = head.next
#         while temp:
#             print(temp.data,end=' ')
#             temp = temp.next
#         print()
#     return head
#
#
# first = [8, 6, 4, 1]
# second = [7, 3, 2]
# third = [9, 5]
# fourth = [12, 11, 10]
# head = create_vertical_list(None, first)


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def merge(a, b):
    curr = Node(-1)
    res = curr
    while a is not None and b is not None:
        if a.data <= b.data:
            curr.bottom = a
            curr = curr.bottom
            a = a.bottom
        else:
            curr.bottom = b
            curr = curr.bottom
            b = b.bottom
    if a is None:
        curr.bottom = b

    if b is None:
        curr.bottom = a

    return res.bottom


def flatten(root):
    if root is None or root.next is None:
        return root
    root.next = flatten(root.next)
    root = merge(root, root.next)
    return root
