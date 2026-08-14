class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we are supposed to use a stack and this stack is gonna pop integers whenever the pointer in the stack encounters a arthematic operator 
        #eg: ["2", "1", "+", "3", "*"]
        stack = []
        for i in tokens: # here i is a pointer
            if i == "+": 
                stack.append(stack.pop() + stack.pop())
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif i == "/":
                a,b = stack.pop() , stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack[-1]
