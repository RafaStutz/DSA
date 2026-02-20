"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        q = deque([root])
        depth = 0
        while q:
            q_size = len(q)
            for element in range(q_size):
                node = q.popleft()
                for child in node.children:
                    q.append(child)

            depth += 1

        return depth

# Time Complexity: O(n) where n is the number of nodes in the tree, as we visit each node once.
# Space Complexity: O(n) in the worst case, if the tree is completely unbalanced.