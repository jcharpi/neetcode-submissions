class MapNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    BUCKET_SIZE = 10000

    def __init__(self):
        self.map = [MapNode(0, 0) for _ in range(self.BUCKET_SIZE)]

    def put(self, key: int, value: int) -> None:
        curr = self.map[key % self.BUCKET_SIZE]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = MapNode(key, value)

    def get(self, key: int) -> int:
        curr = self.map[key % self.BUCKET_SIZE]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.map[key % self.BUCKET_SIZE]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)