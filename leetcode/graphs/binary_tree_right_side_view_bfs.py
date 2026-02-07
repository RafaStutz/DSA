# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        queue = deque([root])
        output = []

        while queue:
            right_side = None
            queue_size_per_level = len(queue)                                     # Number of nodes at the current level

            for element in range(queue_size_per_level):                           # Iterate through nodes at the current level
                node = queue.popleft()                                            
                if node:
                    right_side = node                                             # Update rightmost node seen at this level
                    queue.append(node.left)
                    queue.append(node.right)

            if right_side:
                output.append(right_side.val)

        return output


# Time Complexity: O(n) where n is the number of nodes in the binary tree.
# Space Complexity: O(m) where m is the maximum number of nodes at any level.