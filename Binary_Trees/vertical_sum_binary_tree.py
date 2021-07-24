"""

Calculate horizontal distance of each node from root
Maintain a dictionary with horizontal distance (hd) as key and sum of elements of nodes with that
distance as value
for left child, hd is hd-1
for right child, hd is hd+1

"""


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)


def vertical_util(root, dict1, hd):
    if root is None:
        return
    vertical_util(root.left, dict1, hd - 1)
    if hd in dict1.keys():
        dict1[hd] += root.data
    else:
        dict1[hd] = root.data
    vertical_util(root.right, dict1, hd + 1)


def vertical_sum(root):
    sum_dict = dict()
    vertical_util(root, sum_dict, 0)
    for i, j in sum_dict.items():
        print(i, "=", j, end=", ")


def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    # You can also use strings in list
    list_of_inputs = [15, 12, 14, 7, 20, 27, 88, 23]
    node = build_tree(list_of_inputs)
    vertical_sum(node)
