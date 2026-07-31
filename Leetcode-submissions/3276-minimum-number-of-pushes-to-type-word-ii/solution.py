from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        #we need a counter for this question so well be impoting from collections
        count = Counter(word)
        sorted_counts = sorted(count.values(),reverse = True)
        total_pushes = 0
        for i, freq in enumerate(sorted_counts):
            multipier = (i //8) + 1
            total_pushes += freq * multipier
        return total_pushes
