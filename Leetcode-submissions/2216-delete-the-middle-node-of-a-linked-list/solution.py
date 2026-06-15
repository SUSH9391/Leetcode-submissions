# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        curr = head
        cnt =0
        while curr:
            cnt += 1
            if cnt == (n // 2):
                curr.next = curr.next.next if curr.next.next else None
                break
            curr = curr.next
        return head
