class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = []
        for index, number in enumerate(nums):
            new_list.append([number, index])
        
        new_list.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            current_sum = new_list[l][0] + new_list[r][0]
            if current_sum == target:
                return [min(new_list[l][1], new_list[r][1]),
                        max(new_list[l][1], new_list[r][1])]
            elif current_sum < target:
                l += 1
            else:
                r -= 1
        return []

# Time Complexity: O(n log n) due to sorting the list.
# Space Complexity: O(n) for storing the new list with indices.