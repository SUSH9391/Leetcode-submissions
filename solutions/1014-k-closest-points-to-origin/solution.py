class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #since we are supposed to return the min distace to the origin we are supposed to use minheap which helps us to get this in order of o(n)
        distance = [] #well store a list of distances
        #first lets calculate the distance
        for x,y in points:
            dis = (x ** 2) + (y ** 2)
            distance.append([dis,x,y])
        heapq.heapify(distance)
        res = []
        while k > 0:
            dis,x,y = heapq.heappop(distance)
            res.append([x,y])
            k -=1
        return res
