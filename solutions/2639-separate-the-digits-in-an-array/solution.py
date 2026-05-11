from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            for digit in str(n):
                ans.append(int(digit))

        return ans
