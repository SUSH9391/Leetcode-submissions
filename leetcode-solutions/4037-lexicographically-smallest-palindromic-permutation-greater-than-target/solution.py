from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Check if a palindromic permutation is even possible
        odd_count = sum(1 for v in counts.values() if v % 2 != 0)
        if odd_count > 1:
            return ""
            
        # Available character pairs for the first half of the palindrome
        avail = {chr(i): counts[chr(i)] // 2 for i in range(97, 123)}
        
        # Determine the middle character if the string length is odd
        mid_char = ""
        for k, v in counts.items():
            if v % 2 != 0:
                mid_char = k
                break
                
        half_len = n // 2
        prefix = []
        
        def dfs(idx, is_greater):
            # Base Case: When we've fully constructed the first half
            if idx == half_len:
                if n % 2 != 0:
                    if not is_greater and mid_char < target[idx]:
                        return None
                    next_is_greater = is_greater or (mid_char > target[idx])
                    cur_mid = mid_char
                else:
                    next_is_greater = is_greater
                    cur_mid = ""
                    
                # If prefix is already strictly greater, we are good to go
                if next_is_greater:
                    return cur_mid
                else:
                    # If prefix matches exactly, check if mirrored second half makes it strictly greater
                    full_str = "".join(prefix) + cur_mid + "".join(prefix[::-1])
                    if full_str > target:
                        return cur_mid
                    else:
                        return None
                        
            # Try placing characters from 'a' to 'z'
            for i in range(97, 123):
                c = chr(i)
                if avail[c] > 0:
                    # Skip invalid smaller characters to prevent dipping below target
                    if not is_greater and c < target[idx]:
                        continue
                    
                    # Choose character
                    avail[c] -= 1
                    prefix.append(c)
                    
                    next_is_greater = is_greater or (c > target[idx])
                    res = dfs(idx + 1, next_is_greater)
                    
                    if res is not None:
                        # First valid completion is guaranteed to be lexicographically smallest
                        return c + res
                        
                    # Backtrack
                    prefix.pop()
                    avail[c] += 1
                    
            return None
            
        first_half_and_mid = dfs(0, False)
        
        # If no valid palindrome could be formed that is > target
        if first_half_and_mid is None:
            return ""
            
        # Reconstruct the full string based on parity of n
        if n % 2 != 0:
            first_half = first_half_and_mid[:-1]
            return first_half_and_mid + first_half[::-1]
        else:
            return first_half_and_mid + first_half_and_mid[::-1]
