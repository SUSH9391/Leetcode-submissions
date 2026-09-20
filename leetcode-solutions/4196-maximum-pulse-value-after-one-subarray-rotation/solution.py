class Solution:
    def maxValue(self, nums: List[int]) -> int:
        n = len(nums)
        pulse = 0
        for i in range(n):
            if i % 2 ==0 :
                pulse += nums[i]
            else:
                pulse -= nums[i]
        if n <2:
            return pulse
        prefix = 0
        
        
        min_prefix = [0, None]
        min_even_sum = None
        for i in range(n):
            if i% 2 == 0:
                prefix += nums[i]
            else:
                prefix -= nums[i]
            parity = (i + 1 )% 2
            if min_prefix[parity] is not None:
                current = prefix - min_prefix[parity]
                if min_even_sum is None or current < min_even_sum:
                    min_even_sum = current
            if (min_prefix[parity] is None or prefix > min_prefix[parity]):
                min_prefix[parity] = prefix
        return max(pulse, pulse - 2 * min_even_sum)
        
