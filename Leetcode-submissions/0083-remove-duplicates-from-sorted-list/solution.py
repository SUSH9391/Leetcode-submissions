# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr: #this loop workes till curr becomes 0
            
            if curr.next and curr.next.val == curr.val:
                 # this loop runs till curr.next becomes 0 and the duplicates exit in the value exist 
                curr.next = curr.next.next
            else:
                curr = curr.next # incementing the curr point towards other elements in the linked list
        return head
