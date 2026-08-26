class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        res = ""
        count_of_ones = 0
        l = 0

        for r in range(n):
            if s[r] == '1':
                count_of_ones += 1

            while l <= r and (count_of_ones > k or s[l] == '0'):
                if s[l] == '1':
                    count_of_ones -= 1
                l += 1

            if count_of_ones == k:
                ss = s[l:r + 1]

                if (not res or
                    len(ss) < len(res) or
                    (len(ss) == len(res) and ss < res)):
                    res = ss

        return res
