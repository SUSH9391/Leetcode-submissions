class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] # we mantain a stack to pop the vaild parentsese if its ( we need to pop this )
        res = [] # we need a list where we can display or result
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n :
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN,closedN + 1)
                stack.pop()
        backtrack(0,0)
        return res
