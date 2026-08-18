class Solution:
    def climbStairs(self, n: int) -> int:
        tee, too = 1,1

        #im particularly dynamic programing approach and here im just using an extra space 
        #my very variable names are tee and too so tee points to n-1th element and too points to nth element they are initally one since when we analyse the pattern always the nth and the n-1th step is always 1 simialr to n=0 and n=1 with op as 1
        #what are the next steps that are n-2, n-3 and so on we add the 2 already computed results and move the variable using a temp variable just like fibonnaci series
        for i in range(n-1):
            temp = tee
            tee += too
            too = temp
        return tee
            
            
