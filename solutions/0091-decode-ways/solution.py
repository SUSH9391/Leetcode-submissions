class Solution:
    def numDecodings(self, s: str) -> int:
        #this problem can be solved in 2 ways iterrative dfs or dynamic programming
        #iterrative  dfs is 
        #dp = {len(s) :  1} #intally the 
        #def dfs(i):
            #if i in dp : #if the length of the string is actually 1 then #return dp[1]
                #return dp[i]
            #if s[i] == "0":
                #return 0
            #res = dfs(i + 1)
            #if (i + 1 <len(s) and (s[i] =="1" or s[i] == "2" and s[i+1] #in "0123456")):
                #res += dfs(i+2)
            #dp[i]= res
            #return res
        #return dfs(0)
        dp = {len(s) : 1} 
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if (i+1 <len(s) and(s[i] == '1' or s[i] == '2' and s[i+1] in  "0123456")):
                dp[i] += dp[i+2]
        return dp[0]
