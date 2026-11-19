class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        return min(
            nums[-1] - nums[2],   # Drop 2 smallest
            nums[-3] - nums[0],   # Drop 2 largest
            nums[-2] - nums[1]    # Drop 1 smallest and 1 largest
        )
