class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minval = [inf] * (n-1) + [nums[-1]]
        for i in range(n-2,-1,-1):
            minval[i] = min(minval[i+1],nums[i])
        maxval = 0
        for i in range(n):
            maxval = max(maxval,nums[i])
            if maxval - minval[i] <=k:
                return i
        return -1
