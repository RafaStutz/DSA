class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for n in range(len(nums)):
            for m in range(n + 1, len(nums)):
                if nums[n] + nums[m] == target:
                    return [n, m]
            return []

# Time Complexity: O(n^2) due to the nested loops.
# Space Complexity: O(1) as no extra space is used.