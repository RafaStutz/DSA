# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        values = []
        while q:
            node = q.popleft()
            if node:
                values.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        for element in values:
            if root.val != element:
                return False
        return True
        

# Time Complexity: O(n) because in the worst case we may need to visit all nodes.
# Space Complexity: O(n) in the worst case if the tree is completely unbalanced.