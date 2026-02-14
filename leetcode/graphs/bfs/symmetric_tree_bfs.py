# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root])
        order = []
        while q:
            q_size = len(q)
            level = []
            for _ in range(q_size):
                node = q.popleft()

                if node is None:
                    level.append(None)
                    continue

                level.append(node.val)
                q.append(node.left)
                q.append(node.right)

            low, high = 0, len(level) - 1
            while low < high:
                if level[low] != level[high]:
                    return False
                low += 1
                high -= 1

        return True
        
# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(n) where n is the number of nodes in the tree.
