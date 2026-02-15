# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        depth = 1
        while q:
            q_size = len(q)
            for element in range(q_size):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            depth += 1
        return depth
        
# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(n) where n is the number of nodes in the tree.