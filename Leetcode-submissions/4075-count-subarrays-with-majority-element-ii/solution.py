class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        freq = [0] * (2 * n +1)
        acc = [0] * (2 * n +1)
        freq[n], acc[n] = 1, 1
        bal = n
        res = 0
        for num in nums:
            if num == target: bal += 1
            else: bal -= 1
            freq[bal] += 1
            acc[bal] = acc[bal -1] +freq[bal]
            res += acc[bal - 1]

        return res
