class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def pre_order_traversal(root):
    if root is None:
        return
    print(root.value)
    for child in root.children:
        pre_order_traversal(child)


def depth_first_search(root, target_value):
    if root is None:
        return False
    if root.value == target_value:
        return True
    for child in root.children:
        if depth_first_search(child, target_value):
            return True
    return False


def insert_node(parent_node, child_value):
    if parent_node is None:
        parent_node = child_value
    parent_node.add_child(child_value)


# Example usage:
root = TreeNode(100)
child1 = TreeNode(200)
child2 = TreeNode(375)
root.add_child(child1)
root.add_child(child2)
child1_1 = TreeNode(4000)
child1.add_child(child1_1)     
print("Pre-order Traversal:")
pre_order_traversal(root)
print("Depth First Search for value 4:", depth_first_search(root, 4))
print("Depth First Search for value 4000:", depth_first_search(root, 4000))


    



    