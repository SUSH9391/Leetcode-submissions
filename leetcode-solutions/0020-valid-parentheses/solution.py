class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToopenMap = {')':'(', ']': '[', '}':'{'}
        for c in s:
            if c in closeToopenMap:
                if stack and stack[-1] == closeToopenMap[c]:
                    stack.pop()

                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True
