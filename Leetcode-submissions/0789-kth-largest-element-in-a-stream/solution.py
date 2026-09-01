class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k #we are storing nums in a variable called minHeap basically taking a copy, and copy of k
        heapq.heapify(self.minHeap) #the d.s we use here is heap min heap and use of heapify arranges all the array in sorted list in 0(1)
        while len(self.minHeap) > k: #we are gonna pop kth element based on top of list in o(1)
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) >self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
