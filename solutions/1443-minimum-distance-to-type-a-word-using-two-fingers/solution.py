from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_dist(char1, char2):
            if char1 is None or char2 is None: return 0
            v1, v2 = ord(char1) - ord('A'), ord(char2) - ord('A')
            return abs(v1 // 6 - v2 // 6) + abs(v1 % 6 - v2 % 6)

        @lru_cache(None)
        def solve(i, other_finger):
            if i == len(word):
                return 0
            
            to_pos = word[i]
            prev_pos = word[i-1] if i > 0 else None
            
            # Option 1: Move the finger that typed the previous character
            res1 = get_dist(prev_pos, to_pos) + solve(i + 1, other_finger)
            
            # Option 2: Move the "other" finger
            res2 = get_dist(other_finger, to_pos) + solve(i + 1, prev_pos)
            
            return min(res1, res2)

        return solve(0, None)
