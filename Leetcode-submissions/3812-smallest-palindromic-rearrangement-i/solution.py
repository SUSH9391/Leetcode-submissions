class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        
        count = Counter(s)
        half = []
        mid = ""
        
        for char in sorted(count.keys()):
            freq = count[char]
            half.append(char * (freq // 2))
            if freq % 2 == 1:
                mid = char
                
        left = "".join(half)
        right = left[::-1]
        
        return left + mid + right
