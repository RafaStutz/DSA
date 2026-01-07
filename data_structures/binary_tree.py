class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_child(self, child_node):
        if child_node.value < self.value:
            self.left = child_node
            return
        self.right = child_node


def insert(root, value):
    if root is None:
        root = TreeNode(value)
        return root
    if value < root.value:
        root.left = add_child(root.left, TreeNode(value))                           
    root.right = add_child(root.right, TreeNode(value))
    return root


def pre_order_traversal(root):
    if root is None:
        return
    print(root.value)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)


root = TreeNode(10)
first_child = TreeNode(5)
second_child = TreeNode(15)
root.add_child(first_child)
root.add_child(second_child)    

print(pre_order_traversal(root))
