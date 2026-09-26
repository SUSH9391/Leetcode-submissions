class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        know_dict = {key : val for key, val in knowledge}
        ans = []
        current_key = []
        in_bracket = False
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key_str = "".join(current_key)
                ans.append(know_dict.get(key_str,"?"))
                current_key = []
            else:
                if in_bracket:
                    current_key.append(char)
                else:
                    ans.append(char)
        return "".join(ans)
