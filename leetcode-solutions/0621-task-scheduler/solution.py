from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {} # this is the hashmap that im creating to hold the count of the tasks do the space complexity is o(26)
        for c in tasks:
            count[c] = 1+count.get(c,0)
        output = [-cnt for cnt in count.values()] #[-3,-2,-1]
        heapq.heapify(output)
        time = 0 #time passes so far compleating the tasks
        q = deque() #[('how much of task is remining','at what time this can start')]
        while output or q:
            time += 1 #start time
            if not output and q:
                time = max(time,q[0][1])
            if output:
                cnt = 1+heapq.heappop(output)
                if cnt:
                    q.append([cnt,time+n]) # n is the idel time 
            if q and q[0][1] == time:
                    heapq.heappush(output,q.popleft()[0])
        return time
