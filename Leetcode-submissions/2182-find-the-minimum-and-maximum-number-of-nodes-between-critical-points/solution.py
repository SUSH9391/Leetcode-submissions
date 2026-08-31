# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # A list must have at least 3 nodes to contain a critical point
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        
        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')
        
        index = 1  # Using 0-based indexing where head is 0, so curr is 1
        
        while curr.next:
            nxt = curr.next
            
            # Check if current node is a critical point (local maxima or minima)
            is_local_max = curr.val > prev.val and curr.val > nxt.val
            is_local_min = curr.val < prev.val and curr.val < nxt.val
            
            if is_local_max or is_local_min:
                if first_cp == -1:
                    first_cp = index  # Record the very first critical point
                else:
                    # If it's not the first, we can calculate the distance from the previous one
                    min_dist = min(min_dist, index - prev_cp)
                
                # Update previous critical point to the current one
                prev_cp = index
                
            # Move pointers forward
            prev = curr
            curr = nxt
            index += 1
            
        # If min_dist is still infinity, we found less than 2 critical points
        if min_dist == float('inf'):
            return [-1, -1]
            
        # max_dist is always the difference between the last found cp and the first cp
        max_dist = prev_cp - first_cp
        
        return [min_dist, max_dist]
