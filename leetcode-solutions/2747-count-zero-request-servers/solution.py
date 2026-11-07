class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by time
        logs.sort(key=lambda x: x[1])
        
        # Keep track of original indices of queries so we can place answers back in the correct order
        indexed_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        ans = [0] * len(queries)
        server_counts = {}
        
        left = 0
        right = 0
        m = len(logs)
        active_count = 0
        
        for q_idx, q_time in indexed_queries:
            window_start = q_time - x
            window_end = q_time
            
            # Add logs that fall within or before the window end (<= window_end)
            while right < m and logs[right][1] <= window_end:
                server_id = logs[right][0]
                if server_counts.get(server_id, 0) == 0:
                    active_count += 1
                server_counts[server_id] = server_counts.get(server_id, 0) + 1
                right += 1
                
            # Remove logs that fall outside the window (strictly less than window_start)
            while left < m and logs[left][1] < window_start:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    active_count -= 1
                left += 1
                
            # Servers with zero requests = total servers (n) - active servers
            ans[q_idx] = n - active_count
            
        return ans
