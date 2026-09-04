class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start = 0 
        max_len = 0
        def expand(left,right):
            while left >= 0 and right< len(s) and s[left] ==s[right]:
                left -= 1
                right += 1
            return right - left - 1
        for i in range(len(s)):
            len_odd_string = expand(i,i)
            len_even_string = expand(i,i+1)
            cur_max = max(len_odd_string,len_even_string)
            if cur_max > max_len:
                max_len = cur_max
                start = i-(cur_max - 1)//2
        return s[start: start + max_len]
