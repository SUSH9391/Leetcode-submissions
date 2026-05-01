class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        prev = 0
        total = sum(nums)

        for i in range(n):
            prev += nums[i] * i

        res = prev #this case is for f(0)
        for i in range(n-1, 0 , -1):
            prev = prev + total - n * nums[i]
            res = max(res, prev)

        return res
