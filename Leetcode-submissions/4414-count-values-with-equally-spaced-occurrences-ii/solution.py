class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        map = {}
        res = 0
        for i, n in enumerate(nums):
            if n not in map:
                map[n] = [1,i,i,None,True]
            else:
                occ,first,prev,space,valid = map[n]
                gap = i - prev
                if occ == 1:
                    space = gap
                elif gap != space:
                    valid = False
                map[n] = [occ + 1, first, i ,space,valid]
        for occ, first, prev,space,valid in map.values():
            if occ >= 3 and valid:
                res += 1
        return res
