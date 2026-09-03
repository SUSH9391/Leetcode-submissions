import collections
import heapq


class Solution:

  def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
    # 1. Build directed adjacency list: u -> [(weight, v)]
    adj = collections.defaultdict(list)
    for u, v, w in times:
      adj[u].append((w, v))

    # 2. Min-Heap stores tuples of (cumulative_time, current_node)
    minHeap = [(0, k)]
    visit = set()
    max_time = 0

    while minHeap:
      time, u = heapq.heappop(minHeap)

      if u in visit:
        continue
      visit.add(u)

      # Track the maximum time taken to reach any node
      max_time = max(max_time, time)

      # Explore outgoing edges
      for weight, v in adj[u]:
        if v not in visit:
          # Accumulate the time as we push to the heap
          heapq.heappush(minHeap, (time + weight, v))

    # If we visited all nodes, return the max time; otherwise, signal couldn't reach everyone
    return max_time if len(visit) == n else -1
