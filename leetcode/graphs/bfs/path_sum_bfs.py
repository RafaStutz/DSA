# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        q = deque([(root, targetSum - root.val)])

        while q:
            node, current_sum = q.popleft()
            if node.left is None and node.right is None and current_sum == 0:
                return True
            if node.right:
                q.append((node.right, current_sum - node.right.val))
            if node.left:
                q.append((node.left, current_sum - node.left.val))

        return False
        
# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(n) where n is the number of nodes in the tree.