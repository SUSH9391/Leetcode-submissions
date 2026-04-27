class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices[:] #create a copy of list prices with same elements

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    answer[i] -= prices[j] #dont forget answer is also a list 

                    break
        return answer
