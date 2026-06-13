class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ''
        for i, w in enumerate(words):
            curr = 0 
            for c in w:
                i = ord(c) - ord('a')
                curr += weights[i]
            w = curr % 26
            rev = 25 - w
            res += chr(rev + ord('a'))
        return res
