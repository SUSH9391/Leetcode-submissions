from typing import List

class Solution:
    def findValidElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        valid = [False] * n

        max_left = float('-inf')
        for i in range(n):
            if nums[i] > max_left:
                valid[i] = True
            max_left = max(max_left, nums[i])

        
        max_right = float('-inf')
        for i in range(n - 1, -1, -1):
            if nums[i] > max_right:
                valid[i] = True
            max_right = max(max_right, nums[i])

        return [nums[i] for i in range(n) if valid[i]]
