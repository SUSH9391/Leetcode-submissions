class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()

        for i in range(n):
            for j in range(i, n):
                seen.add(nums[i] ^ nums[j])
        res = set()
        for i in range(n):
            for v in seen:
                res.add(nums[i] ^ v)
        return len(res)
