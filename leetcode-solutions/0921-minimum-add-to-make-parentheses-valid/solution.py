class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        #we have to see how will the parenthesis string will be vaild so the parenthesis sting will be valid 
        #we are supposed to solve this in O(1) space
        # we track two things open_count, add_needed
        open_count = 0
        add_needed = 0
        for c in s:
            if c == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    add_needed += 1
        return add_needed+open_count
