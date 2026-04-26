class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #creating an empty list in the form of list
        expression = []
        #remember to always have a variable ans where u can use this to get the final answer
        for i in tokens:
            if i not in "+-*/":
                expression.append(int(i))
            else:
                item1 = expression.pop()
                item2 = expression.pop()

                match i:
                    case "+":
                        expression.append(item1 + item2)
                    case "-":
                        expression.append(item2 - item1)
                    case "*":
                        expression.append(item1 * item2)
                    case "/":
                        expression.append(int(item2 / item1)) #truncate towards 0 only int allowwed
        return expression[-1]
