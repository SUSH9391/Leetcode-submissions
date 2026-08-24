class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Calculate prefix sums in-place to save space (or use a new array)
        prefix = stones[:]
        for i in range(1, n):
            prefix[i] += prefix[i - 1]
            
        # The base case: If the game reaches the last possible valid move, 
        # the player MUST take all remaining stones (index n-1).
        # The opponent gets 0 points.
        ans = prefix[-1]
        
        # Work backwards from the second-to-last index down to index 1.
        # (Index 0 is skipped because a player must remove at least x > 1 stones)
        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)
            
        return ans
