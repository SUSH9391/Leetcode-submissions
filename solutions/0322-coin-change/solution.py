class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp is an array here we are implementing the dynamic programing appch with memorization kinda brure force technique
        dp = [amount+1] * (amount +1)
        dp[0] = 0 #if amount is zero we need zero coins
        for a in range(1,amount+1):
            #this is a for loop which runs on dp array which keeps track of amount
            for c in coins:
                #this is a for loop which runs on current coins array to keep tack of current denominations
                if a-c >= 0:
                    dp[a] = min(dp[a] , 1+dp[a-c])
                #if we have amount = 7 and coin currently is 2 then the result is 5 so we take the dp[7] = 1+dp[2]
        return dp[amount] if dp[amount]!= amount + 1 else -1
