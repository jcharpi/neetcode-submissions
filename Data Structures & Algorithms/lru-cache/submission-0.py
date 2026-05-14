class LRUNode:
    def __init__(self, key, value, prev = None, nxt = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.tail = LRUNode(0, 0)
        self.head = LRUNode(0, 0)
        self.tail.prev = self.head
        self.head.next = self.tail
        self.size = capacity
        self.hm = {}

    def remove(self, node: LRUNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def enqueue(self, node: LRUNode):
        self.tail.prev.next = node
        node.prev = self.tail.prev

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hm:
            self.remove(self.hm[key])
            self.enqueue(self.hm[key])
            return self.hm[key].value
        return -1

    def put(self, key: int, value: int) -> None:
            if key in self.hm:
                self.remove(self.hm[key])
                self.hm[key].value = value
            else:
                if len(self.hm.keys()) == self.size:
                    self.hm.pop(self.head.next.key)
                    self.remove(self.head.next)
                self.hm[key] = LRUNode(key, value)
            self.enqueue(self.hm[key])


