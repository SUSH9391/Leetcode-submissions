class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k+1):
            tmpPrices = prices[:]
            for u,v,w in flights:
                if prices[u] == float("inf"):
                    continue
                if prices[u] + w <tmpPrices[v]:
                    tmpPrices[v] = prices[u] + w
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]
