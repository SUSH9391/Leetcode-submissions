import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        # Precompute LCM and subset sizes for all 2^n - 1 non-empty subsets
        subsets = []
        for i in range(1, 1 << n):
            curr_lcm = 1
            set_bits = 0
            for j in range(n):
                if i & (1 << j):
                    curr_lcm = math.lcm(curr_lcm, coins[j])
                    set_bits += 1
            subsets.append((curr_lcm, set_bits))
            
        def count_amounts_up_to(x: int) -> int:
            """Calculates how many amounts <= x can be formed using the coins."""
            count = 0
            for curr_lcm, set_bits in subsets:
                # Add if odd number of elements, subtract if even (PIE)
                if set_bits % 2 == 1:
                    count += x // curr_lcm
                else:
                    count -= x // curr_lcm
            return count

        # Binary search for the kth smallest amount
        left = 1
        right = min(coins) * k
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if count_amounts_up_to(mid) >= k:
                ans = mid
                right = mid - 1  # Try to find a smaller valid amount
            else:
                left = mid + 1   # We need more amounts, increase the search space
                
        return ans
