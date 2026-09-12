class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        valid_count = 0
        for _ in range(n):
            score = 0
            for i in range(n-1):
                if s[i] == s[i+1]:
                    score += 1
            if score == k:
                valid_count += 1
            s = s[1:] + s[0]
        return valid_count
