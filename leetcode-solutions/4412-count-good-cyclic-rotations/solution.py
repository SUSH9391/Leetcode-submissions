class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        k = n // 2
        arr = nums+nums
        prefix = [0] * (2 * n +1)
        for i in range(2*n):
            prefix[i+1] = prefix[i] + arr[i]
        good_rotations = 0
        for i in range(n):
            left_sum = prefix[i+k] - prefix[i]
            right_sum = prefix[i+n] - prefix[i+k]
            if left_sum > right_sum:
                good_rotations += 1
        return good_rotations
