class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Map key -> Node
        
        # Dummy head and tail to mark the boundaries of our doubly linked list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper: Remove an existing node from its current spot in the linked list
    def _remove(self, node: Node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # Helper: Insert a node right at the front (Most Recently Used position, just after head)
    def _add_to_front(self, node: Node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Mark it as recently used by moving it to the front
            self._remove(node)
            self._add_to_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> int:
        if key in self.cache:
            # Update the existing node and move it to the front
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            # Create a new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
            
            # Check if we exceeded capacity
            if len(self.cache) > self.capacity:
                # Evict the least recently used node (the one right before tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
