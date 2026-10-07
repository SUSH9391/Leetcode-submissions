class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        #here we need to score based on how many det of parenthesis match 
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                v = stack.pop()
                score = max(2*v,1)
                stack[-1] += score
        return stack[0]
