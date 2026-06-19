class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res  = 0
        acc = 0
        for g in gain:
            acc += g
            res = max(res, acc)
        return res
