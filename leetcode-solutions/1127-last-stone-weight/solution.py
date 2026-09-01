class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #well be using max heap to return the max weighted stone so since in python we dont have maxheap well be multipying to -ve and use minheap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1: #since we need pair of stones
            first_stone = heapq.heappop(stones)
            second_stone = heapq.heappop(stones)
            if second_stone >first_stone:
                heapq.heappush(stones,(first_stone - second_stone))
        stones.append(0)
        return abs(stones[0])
