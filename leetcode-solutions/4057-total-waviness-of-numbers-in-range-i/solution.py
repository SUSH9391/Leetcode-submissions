class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
        
        for num in range(num1, num2 + 1):
            if num < 100:
                continue
            
            s = str(num)
            for i in range(1, len(s) - 1):
                prev = int(s[i-1])
                curr = int(s[i])
                nxt = int(s[i+1])
                
                if curr > prev and curr > nxt:
                    total_waviness += 1
                elif curr < prev and curr < nxt:
                    total_waviness += 1
                    
        return total_waviness
