class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # stright forward  elimination if not the string's length is not equal
        #idea : visit the array twice and store the values in hashmap and compare the hasmap
        # time complexity : O(s + t) ~ O(2n) ~ O(n)
        # sapce complexity : O(s + t) ~ O(2n) ~ O(n)
        # hows the hasmap gonna look is {key - char : times - count}
        countS, countT = {}, {} # initalized two hashmap
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) # eg is a is visited for the 1st time and a apperes again then we do 1 + 1 = 2 else 1+0 = 1
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False # eg countS[a] = 2 and countT[a] = 1 so return False else countS[a] = 2 and countT[a] dosent exist then compare 2 and 0 which is false
        return True
