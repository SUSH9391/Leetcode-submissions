class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini = nums.index(min(nums))
        maxi = nums.index(max(nums))
        l = min(maxi,mini)
        r = max(maxi, mini)
        n = len(nums)
        return min(r+1, n-l, l+1+n-r)

