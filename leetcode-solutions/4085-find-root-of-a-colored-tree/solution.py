from collections import deque, defaultdict

class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        #approach: to find valid root node that satisfier both the binary tree property and layered color pattern
        #1st adjacenccy list to be build using a hashset each node in bin tree has a degree of 3 atmost 2 + 1
        #color pattern  r->b->w->r->b->w->r...
        n = len(colors)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Degree pruning: Root can have at most 2 children (degree <= 2)
        # Other nodes can have at most 1 parent + 2 children (degree <= 3)
        candidates = []
        for i in range(n):
            deg = len(adj[i])
            if deg > 3:
                return -1
            if deg <= 2:
                candidates.append(i)
                
        c_map = {'R': 0, 'B': 1, 'W': 2}
        
        def isValid(root):
            root_color_val = c_map[colors[root]]
            queue = deque([(root, -1, 0)])
            visited_count = 0
            
            while queue:
                curr, parent, dept = queue.popleft()
                visited_count += 1
                
                if c_map[colors[curr]] != (root_color_val + dept) % 3:
                    return False
                
                children = 0
                for nei in adj[curr]:
                    if nei != parent:
                        children += 1
                        queue.append((nei, curr, dept + 1))
                
                if children > 2:
                    return False
                    
            return visited_count == n

        for root in candidates:
            if isValid(root):
                return root
                
        return -1
