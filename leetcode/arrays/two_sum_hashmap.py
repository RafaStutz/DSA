class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
            
# Time Complexity: O(n) because we traverse the list once.
# Space Complexity: O(n) for storing elements in the hashmap.