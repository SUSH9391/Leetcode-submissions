from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
        
        queue = deque([0])
        visited = set([0])
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                
                if i == n - 1:
                    return steps
                
                
                neighbors = []
                
                if i + 1 < n:
                    neighbors.append(i + 1)
                if i - 1 >= 0:
                    neighbors.append(i - 1)
                
                neighbors.extend(graph[arr[i]])
                
                for nei in neighbors:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
                
                graph[arr[i]].clear()
            
            steps += 1
        
        return -1
