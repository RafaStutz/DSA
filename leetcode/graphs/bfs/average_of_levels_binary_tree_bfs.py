# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        queue = deque([root])
        result = []
        while queue:
            queue_size = len(queue)
            level_sum = 0
            for element in range(queue_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            average = level_sum / queue_size
            result.append(average)
        return result
        
# Time Complexity: O(n) because we visit each node once.
# Space Complexity: O(n) in the worst case.