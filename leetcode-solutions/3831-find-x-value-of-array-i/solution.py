class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k
        
        for num in nums:
            next_dp = [0] * k
            
            # Subarray starting at the current element
            next_dp[num % k] += 1
            
            # Extend existing subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * num) % k
                    next_dp[new_r] += dp[r]
            
            dp = next_dp
            
            # Add current step's counts to the overall result
            for r in range(k):
                result[r] += dp[r]
                
        return result
