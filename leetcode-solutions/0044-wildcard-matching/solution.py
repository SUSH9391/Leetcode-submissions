class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        i, j = 0, 0
        star_idx = -1
        s_checkpoint = -1
        
        while i < s_len:
            # Case 1: Direct match or '?'
            if j < p_len and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            # Case 2: '*' encountered
            elif j < p_len and p[j] == '*':
                star_idx = j
                s_checkpoint = i
                j += 1
            # Case 3: Mismatch, but we have a '*' to fall back on
            elif star_idx != -1:
                j = star_idx + 1
                s_checkpoint += 1
                i = s_checkpoint
            # Case 4: Mismatch and no '*' available
            else:
                return False
                
        # Consume any remaining trailing '*' in the pattern
        while j < p_len and p[j] == '*':
            j += 1
            
        return j == p_len
