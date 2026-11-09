import bisect
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Min-heap to track active servers: stores (free_time, server_id)
        busy_servers = []
        
        # Available servers pool, initially all servers from 0 to k-1
        available = list(range(k))
        
        request_counts = [0] * k
        
        for i in range(len(arrival)):
            curr_time = arrival[i]
            duration = load[i]
            
            # Free up servers whose tasks have finished by curr_time
            while busy_servers and busy_servers[0][0] <= curr_time:
                _, server_id = heapq.heappop(busy_servers)
                # Insert back into available servers maintaining sorted order
                idx = bisect.bisect_left(available, server_id)
                available.insert(idx, server_id)
            
            # If no servers are available, drop the request
            if not available:
                continue
            
            # Find the first available server >= (i % k)
            target = i % k
            idx = bisect.bisect_left(available, target)
            
            # If none found >= target, wrap around to the beginning of the available list
            if idx == len(available):
                idx = 0
            
            server_id = available.pop(idx)
            
            # Assign the request to this server
            request_counts[server_id] += 1
            heapq.heappush(busy_servers, (curr_time + duration, server_id))
            
        max_requests = max(request_counts)
        return [i for i, count in enumerate(request_counts) if count == max_requests]
