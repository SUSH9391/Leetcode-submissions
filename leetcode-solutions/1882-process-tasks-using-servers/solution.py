class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        res = [0] * len(tasks)
        avail = [(servers[i],i)for i in range(len(servers))]
        heapq.heapify(avail)
        unavial = []
        t = 0
        for i in range(len(tasks)):
            t = max(i,t)
            if len(avail) == 0:
                t = unavial[0][0]
            while unavial and t >= unavial[0][0]:
                timefree,weight,index = heapq.heappop(unavial)
                heapq.heappush(avail,(weight,index))
            weight, index = heapq.heappop(avail)
            res[i] = index
            heapq.heappush(unavial,(t+tasks[i],weight,index))
        return res
