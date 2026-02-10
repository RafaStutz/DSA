# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()
        if root:
            queue.append(root)
        
        order = []

        while queue:
            level = []

            for element in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                order.append(level)

        return order
        

# Time Complexity: O(n) because we visit each node once.
# Space Complexity: O(n) in the worst case.