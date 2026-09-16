class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        cur_line, cur_line_len = [], 0
        i = 0
        
        while i < len(words):
            # Line complete
            if cur_line_len + len(cur_line) + len(words[i]) > maxWidth:
                extra_space = maxWidth - cur_line_len
                gaps = max(1, len(cur_line) - 1) # Number of gaps between words
                
                spaces = extra_space // gaps
                remainder = extra_space % gaps
                
                for j in range(gaps):
                    cur_line[j] += " " * spaces
                    if remainder:
                        cur_line[j] += " "
                        remainder -= 1
                        
                res.append("".join(cur_line))
                cur_line, cur_line_len = [], 0
            
            cur_line.append(words[i])
            cur_line_len += len(words[i])
            i += 1
            
        # Handle the last line (Left-justified)
        last_line = " ".join(cur_line)
        trailing_space = maxWidth - len(last_line)
        res.append(last_line + " " * trailing_space)
        
        return res
