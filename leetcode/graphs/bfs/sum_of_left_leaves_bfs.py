# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        is_left_child =  False
        q = deque([(root, is_left_child)])
        left_leaf_sum = 0
        while q:
            for _ in range(len(q)):
                node, is_left_child = q.popleft()
                if not node.left and not node.right and is_left_child:
                    left_leaf_sum += node.val
                if node.left:
                    is_left_child = True
                    q.append((node.left, is_left_child))
                if node.right:
                    is_left_child = False
                    q.append((node.right, is_left_child))

        return left_leaf_sum
        
# Time Complexity: O(n) where n is the number of nodes in the tree, as we visit each node once.
# Space Complexity: O(n) in the worst case, if the tree is completely unbalanced.