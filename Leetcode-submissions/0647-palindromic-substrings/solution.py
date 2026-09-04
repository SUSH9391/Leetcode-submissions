class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        for i in range(len(s)):
            res += self.isPali(s,i,i) #odd lenght
            res += self.isPali(s,i,i+1) #even lenght
        return res
    def isPali(self,s,l,r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res+=1
            l -= 1
            r += 1
        return res
