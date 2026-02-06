# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        queue = deque([(root1, root2)])
        
        while queue:
            n1, n2 = queue.popleft()
            
            n1.val += n2.val
        
            if n1.left is None:
                n1.left = n2.left
            elif n2.left is not None:
                queue.append((n1.left, n2.left))
            
            if n1.right is None:
                n1.right = n2.right
            elif n2.right is not None:
                queue.append((n1.right, n2.right))

        return root1


# Time Complexity: O(n) where n is the number of nodes in the smaller tree.
# Merge in-place, so no additional space is used for the merged tree
# Space Complexity: O(m) where m is the number of nodes in the queue at any time.