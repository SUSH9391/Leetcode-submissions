import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            # Find the index of the smallest element >= num
            idx = bisect.bisect_left(sub, num)
            
            # If num is larger than all elements in sub, append it
            if idx == len(sub):
                sub.append(num)
            else:
                # Otherwise, replace the existing element to keep potential tails small
                sub[idx] = num
                
        return len(sub)
