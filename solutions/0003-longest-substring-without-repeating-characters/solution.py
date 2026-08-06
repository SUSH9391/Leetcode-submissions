from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringSet = set()
        queue = deque()
        maxLength = 0
        for c in s:
            while c in stringSet:
                popped_char = queue.popleft()
                stringSet.remove(popped_char)
            queue.append(c)
            stringSet.add(c)

            maxLength = max(maxLength, len(queue))
        return maxLength
