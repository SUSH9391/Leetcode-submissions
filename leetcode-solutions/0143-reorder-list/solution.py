# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            t = second.next
            second.next = prev
            prev = second
            second = t
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2
        
