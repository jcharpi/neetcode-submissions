class LRUNode:
    def __init__(self, key, val, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.head = LRUNode(0, 0)
        self.tail = LRUNode(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}
        self.capacity = capacity

    def remove(self, node: LRUNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_end(self, node: LRUNode):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.move_to_end(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
        else: 
            if len(self.cache) == self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]

            node = LRUNode(key, value)
            self.cache[key] = node
        self.move_to_end(node)