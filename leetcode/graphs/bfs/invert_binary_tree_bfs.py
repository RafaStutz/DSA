# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.right, node.left = node.left, node.right

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return root
            

# Time Complexity: O(n) because we visit each node once.
# Space Complexity: O(n) in the worst case.