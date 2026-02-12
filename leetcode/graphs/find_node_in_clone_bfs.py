# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque([(original, cloned)])

        while q:
            
            o, c = q.popleft()
            if o:
                q.append((o.left, c.left))
                q.append((o.right, c.right))
            if o is target:
                return c

        return None

# Time Complexity: O(n) because in the worst case we may need to visit all nodes.
# Space Complexity: O(n) in the worst case if the tree is completely unbalanced.