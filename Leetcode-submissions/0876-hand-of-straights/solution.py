class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: #if this returns true you cant divide the hand array into group size
            return False
        count = {} #hashmap to hold the number of each cards present in the hand array
        for n in hand:
            count[n] = 1 + count.get(n,0) #if it dosent exist 1+0
        minHeap = list(count.keys()) # the keys of the hashmap has the card numbers and these card numbers we are storing in a min heap so that everytime we return the min card in order of logn in worst case it can be done is linear time also but we encourage logn convert this in to 
        heapq.heapify(minHeap) # this will be stored in minheap 
        while minHeap:
            first_elem = minHeap[0] #since its a list of dtype minheap
            for i in range(first_elem, first_elem + groupSize): #because we need exactly first - first + groupsize
                if i not in count:
                    return False # 1,2,4 3 dosent exits then return false
                count[i] -= 1 #when we finish visiting we decrement the count and we pop the value of heap and if the heap is not the top of the list
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True

