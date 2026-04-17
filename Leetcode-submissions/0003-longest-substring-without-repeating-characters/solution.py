class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # If we find a duplicate, shrink the window from the left
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
        
            # Add the current character and update max_length
            charSet.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
