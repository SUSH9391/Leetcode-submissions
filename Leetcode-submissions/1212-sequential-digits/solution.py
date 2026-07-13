class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        c = '123456789' #sequential numbers
        res = [] #result is a list 
        for i in range(9):
            for j in range(i, 9): # j is after i
                #curr = c[i : j+1]
                curr = ""
                for k in range(i, j+1):
                    curr += c[k]
                num = int(curr) #convert str to num
                if low<= num <= high: res.append(num) #check if numersin range
        res.sort()
        return res
