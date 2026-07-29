import collections

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        MAX_K = 10**6 + 1
        count = collections.Counter(s)
        
        # Check odd frequency counts
        odd_chars = [c for c, freq in count.items() if freq % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        # We only need to arrange half of each character frequency
        half_count = [0] * 26
        for c, freq in count.items():
            half_count[ord(c) - ord('a')] = freq // 2

        # Helper to compute combinations nCk capped at MAX_K
        def nCk(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            res = 1
            for i in range(1, min(r, n - r) + 1):
                res = res * (n - i + 1) // i
                if res >= MAX_K:
                    return MAX_K
            return res

        # Helper to calculate total distinct arrangements for remaining character counts
        def count_arrangements(counts: list[int]) -> int:
            total = sum(counts)
            res = 1
            for freq in counts:
                if freq == 0:
                    continue
                res *= nCk(total, freq)
                if res >= MAX_K:
                    return MAX_K
                total -= freq
            return res

        # 1. Validate if there are enough total permutations
        total_permutations = count_arrangements(half_count)
        if k > total_permutations:
            return ""

        # 2. Construct the left half character-by-character
        left_half = []
        half_len = sum(half_count)

        for _ in range(half_len):
            for i in range(26):
                if half_count[i] == 0:
                    continue
                
                # Try placing char 'a' + i
                half_count[i] -= 1
                ways = count_arrangements(half_count)
                
                if ways >= k:
                    left_half.append(chr(i + ord('a')))
                    break
                else:
                    k -= ways
                    half_count[i] += 1  # Backtrack and try next character

        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]
