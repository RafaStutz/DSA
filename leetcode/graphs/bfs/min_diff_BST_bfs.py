# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        vals = []

        while q:
            node = q.popleft()
            vals.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        vals.sort()
        diff = float("inf")
        for i in range(1, len(vals)):
            diff = min(diff, vals[i] - vals[i - 1])
        
        return diff if diff != float("inf") else 0
           

# Time Complexity: O(n log n) due to sorting the values.
# Space Complexity: O(n) for storing the values of the nodes.