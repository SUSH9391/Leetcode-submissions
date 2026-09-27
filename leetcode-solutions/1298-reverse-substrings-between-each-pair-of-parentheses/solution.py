class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                temp = []
                # Pop characters until we find the matching '('
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                
                # Pop the '(' itself
                stack.pop() 
                
                # Add the reversed characters back to the stack.
                # Note: They are already reversed because of how pop() works.
                stack.extend(temp)
            else:
                stack.append(char)
                
        return "".join(stack)
