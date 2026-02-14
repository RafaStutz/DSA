# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

        if not root:
            return

        root.val = 0
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                node.left.val = 1 + node.val * 2
                q.append(node.left)
            if node.right:
                node.right.val = 2 + node.val * 2
                q.append(node.right)
        

    def find(self, target: int) -> bool:
        root = self.root

        if not root:
            return False

        q = deque([root])

        while q:
            node = q.popleft()
            if node.val == target:
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return False

# Time Complexity: O(n) for the constructor and O(n) for the find method in the worst case.
# Space Complexity: O(n) for the constructor and O(n) for the find method in the worst case.