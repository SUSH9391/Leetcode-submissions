class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            instability = max(nums[0:i+1]) - min(nums[i:len(nums)])
            if instability <= k:
                return i
        return -1
        
        
