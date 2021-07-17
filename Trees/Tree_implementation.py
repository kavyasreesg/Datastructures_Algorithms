# hierarchically representing objects/items
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        # Count number of ancestors
        p = self.parent
        level = 0
        while p:
            p = p.parent
            level += 1
        return level

    def print_tree(self):
        # Print in hierarchy
        # utilise the level of nodes
        level = self.get_level()
        spaces = '  ' * level * 3
        prefix = spaces + '|__>' if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root_node = TreeNode("Electronics")
    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("Macbook"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("ThinkPad"))
    mobile = TreeNode("Cell Phones")
    mobile.add_child(TreeNode("iphone"))
    mobile.add_child(TreeNode("Google pixel"))
    mobile.add_child(TreeNode("Vivo"))
    root_node.add_child(mobile)
    root_node.add_child(laptop)
    return root_node


root = build_tree()
root.print_tree()
pass
