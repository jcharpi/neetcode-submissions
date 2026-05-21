class SetNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [SetNode(0) for _ in range(10000)]

    def add(self, key: int) -> None:
        curr = self.set[key % len(self.set)]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = SetNode(key)

    def remove(self, key: int) -> None:
        curr = self.set[key % len(self.set)]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.set[key % len(self.set)]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)