class Solution:

  def findItinerary(self, tickets: list[list[str]]) -> list[str]:
    # 1. Build adjacency list and sort targets in reverse order
    # (so we can pop the alphabetically smallest from the end in O(1))
    adj = collections.defaultdict(list)
    for src, dst in sorted(tickets, reverse=True):
      adj[src].append(dst)

    res = []

    def dfs(curr):
      # While this airport still has outgoing flights, visit them
      while adj[curr]:
        next_airport = adj[curr].pop()
        dfs(next_airport)
      # Once out of flights, add to result (dead-end first)
      res.append(curr)

    dfs("JFK")
    # Since we recorded from the dead end back to the start, reverse it
    return res[::-1]
