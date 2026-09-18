class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Pre-calculate the absolute first and last index of every character
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
            
        valid_intervals = []
        
        # Step 2: Find all valid, fully-expanded ranges
        for i, char in enumerate(s):
            # Only start building a chunk from a character's very first occurrence
            if i == first[char]:
                end = last[char]
                j = i
                is_valid = True
                
                while j <= end:
                    # THE TRAP: If a character inside our box started before our box, it's invalid
                    if first[s[j]] < i:
                        is_valid = False
                        break
                    
                    # THE EXPANSION: Push the end boundary out if necessary
                    end = max(end, last[s[j]])
                    j += 1
                
                # If we made it through without breaking, save the valid interval
                if is_valid:
                    valid_intervals.append((i, end))
                    
        # Step 3: Greedy Selection (Interval Scheduling)
        # Sort by the 'end' index to always pick the chunk that finishes earliest
        valid_intervals.sort(key=lambda x: x[1])
        
        res = []
        last_end = -1
        
        for start, end in valid_intervals:
            # If this chunk starts after our last selected chunk ended, we can take it!
            if start > last_end:
                res.append(s[start:end+1])
                last_end = end
                
        return res
