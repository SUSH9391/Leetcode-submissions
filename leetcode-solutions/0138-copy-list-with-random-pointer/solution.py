"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        #im creating the hashmap first to map to original node to the copy node or to show the cloning
        oldTonew = {}
        curr = head
        while curr:
            copy = Node(curr.val) #so the idea is to first store the value of the node to the hashmap then run pass 2 to map the pointers to next and random since these random pointers might point to any node forward or backward in the case of forward it might be 2 or 3 steps forward so the node will not or hasnt been created 
            oldTonew[curr] = copy #{old : curr[val i.e., copy]}
            curr = curr.next # travese through entier list
        curr = head #bring the current pointer back to head
        while curr: #while curent is none
            copy = oldTonew[curr]
            copy.next = oldTonew[curr.next] if curr.next else None
            copy.random = oldTonew[curr.random] if curr.random else None
            curr = curr.next
        return oldTonew[head]
