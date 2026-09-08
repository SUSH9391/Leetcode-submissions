class Solution:
    def countRotations(self, s: str, k: int) -> int:
        #whenever we rotate the strings the adjeacent pain of strings if equal will score to 0 so this is one of the base case
        #another base case is we return the score which is equal to k k is given in the input 
        #if k == no_of_equal:
            #res = number of unequal pairs
        #elif k == e-1:
        #res= no of equal edges
        #else : 0
        n = len(s)
        if n ==0:
            return 0
        eq = sum (s[i] == s[(i+1)% n] for i in range(n))
        if k == eq:
            return n- eq
        elif k ==eq -1:
            return eq
        else:
            return 0
        
