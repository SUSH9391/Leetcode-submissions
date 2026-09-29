class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length= 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    current_len = i-stack[-1]
                    max_length = max(max_length,current_len)
        return max_length
