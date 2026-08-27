class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        # Step 1: Create a frequency array for available characters in s
        count = [0] * 26
        for char in s:
            count[ord(char) - 97] += 1
            
        # Step 2: Greedily find the longest matching prefix
        i = 0
        while i < n and count[ord(target[i]) - 97] > 0:
            count[ord(target[i]) - 97] -= 1
            i += 1
            
        # Step 3: Set our starting index j to backtrack from
        j = min(i, n - 1)
        
        # If we matched the entire string exactly, we need to backtrack from the last character.
        # Put the last character back into our "available" count before evaluating it.
        if i == n:
            count[ord(target[n - 1]) - 97] += 1
            
        # Step 4: Backtrack right-to-left to find the first place we can bump the character
        while j >= 0:
            target_char_idx = ord(target[j]) - 97
            
            # Look for the smallest available character STRICTLY greater than target[j]
            for k in range(target_char_idx + 1, 26):
                if count[k] > 0:
                    # Found a larger character! Place it here.
                    count[k] -= 1
                    
                    # Sort the rest of the available characters to ensure it's the smallest possible string
                    suffix = []
                    for char_idx in range(26):
                        if count[char_idx] > 0:
                            suffix.append(chr(char_idx + 97) * count[char_idx])
                            
                    # Construct and return the final string
                    return target[:j] + chr(k + 97) + "".join(suffix)
            
            # If we couldn't bump at index j, we must backtrack further.
            # "Un-match" the previous character and add it back to our available count.
            if j > 0:
                count[ord(target[j - 1]) - 97] += 1
            j -= 1
            
        # If we backtrack all the way to -1 without returning, no greater permutation exists.
        return ""
