class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        # Count the frequencies of remainders
        counts = [0, 0, 0]
        for stone in stones:
            counts[stone % 3] += 1
            
        # Case 1: Even number of multiples of 3
        if counts[0] % 2 == 0:
            # Alice wins as long as she has both 1s and 2s to choose from
            return counts[1] > 0 and counts[2] > 0
            
        # Case 2: Odd number of multiples of 3
        else:
            # Alice needs a significant imbalance to force Bob into a losing move
            return abs(counts[1] - counts[2]) > 2
