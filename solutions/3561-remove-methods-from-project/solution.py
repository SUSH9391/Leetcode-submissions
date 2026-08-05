class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        # Step 2: Find all suspicious methods using DFS/BFS starting from k
        suspicious = set()
        stack = [k]
        suspicious.add(k)
        
        while stack:
            curr = stack.pop()
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    stack.append(neighbor)
                    
        # Step 3: Check if any method outside the suspicious set invokes a suspicious method
        is_valid = True
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                is_valid = False
                break
                
        # Step 4: Return the result
        if not is_valid:
            return list(range(n))
        
        return [i for i in range(n) if i not in suspicious]
