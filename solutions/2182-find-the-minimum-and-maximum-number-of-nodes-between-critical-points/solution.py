# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        prev = head
        cur = head.next
        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')
        index = 1
        while cur.next:
            nxt = cur.next
            isLocalmin = cur.val< prev.val and cur.val<nxt.val
            isLocalmax = cur.val> prev.val and cur.val>nxt.val
            if isLocalmax or isLocalmin:
                if first_cp == -1:
                    first_cp = index
                else:
                    min_dist = min(min_dist, index - prev_cp)
                prev_cp = index
            prev = cur
            cur = nxt
            index += 1
        if min_dist == float('inf'):
            return [-1, -1]
        max_dist = prev_cp - first_cp
        return [min_dist, max_dist]
