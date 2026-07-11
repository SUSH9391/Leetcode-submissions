class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)
        def dfs(node):
            seen.add(node)
            component.append(node)
            for nei in adj[node]:
                if not nei in seen: dfs(nei)
        res = 0
        seen = set()
        for node in range(n):
            if not node in seen:
                component = []
                dfs(node)
                c = len(component)
                valid = True
                for i in range(c):
                    for j in range(i + 1, c):
                        if not component[i] in adj[component[j]]:
                            valid = False
                            break
                if valid : res += 1
        return res
