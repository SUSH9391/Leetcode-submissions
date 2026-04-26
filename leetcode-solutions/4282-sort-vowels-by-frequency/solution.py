from typing import List
from collections import Counter

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiou')
        glanvoture = s
        vowel_list = [ch for ch in s if ch in vowels]
        freq = Counter(vowel_list)
        first_pos = {}
        for i, ch in enumerate(s):
            if ch in vowels and ch not in first_pos:
                first_pos[ch] = i
        sorted_vowels = sorted(
            vowel_list,
            key=lambda ch: (-freq[ch], first_pos[ch])
        )
        result = list(s)
        j = 0
        for i in range(len(result)):
            if result[i] in vowels:
                result[i] = sorted_vowels[j]
                j += 1
        
        return ''.join(result)
