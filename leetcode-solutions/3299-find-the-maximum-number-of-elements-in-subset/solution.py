class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        fm = defaultdict(int)
        for num in nums:fm[num] += 1
        ones = fm[1]
        res = ones if ones % 2 == 1 else max(0, ones - 1)

        for num in fm:
            if num == 1:continue

            total = 0
            curr = num
            while curr in fm and fm[curr] >= 2:
                total += 2
                curr *= curr
            if curr in fm: total +=1
            elif not curr in fm: total -= 1
            res = max(res, total)
        return res
                
