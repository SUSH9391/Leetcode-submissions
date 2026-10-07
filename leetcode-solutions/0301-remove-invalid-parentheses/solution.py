class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        if not s:
            return [""]

        visited = {s}
        queue = [s]
        res = []
        found = False

        while queue:
            next_level = []
            for curr in queue:
                if isValid(curr):
                    res.append(curr)
                    found = True
            
            # If we found valid strings at this depth, stop going deeper
            if found:
                break

            for curr in queue:
                for i in range(len(curr)):
                    if curr[i] in ('(', ')'):
                        # Generate all possible strings by removing one parenthesis
                        next_str = curr[:i] + curr[i+1:]
                        if next_str not in visited:
                            visited.add(next_str)
                            next_level.append(next_str)
            
            queue = next_level

        return res
