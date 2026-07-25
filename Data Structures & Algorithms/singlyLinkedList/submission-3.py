class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:    
    def __init__(self):
        self.head = ListNode()
    
    def get(self, index: int) -> int:
        curr = self.head.next
        for i in range(index):
            if not curr:
                return -1
            curr = curr.next
        return curr.val if curr else -1

    def insertHead(self, val: int) -> None:
        self.head.next = ListNode(val, self.head.next)

    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def remove(self, index: int) -> bool:
        prev = self.head
        for i in range(index):
            if not prev.next:
                return False
            prev = prev.next

        if not prev.next:
            return False

        prev.next = prev.next.next 
        return True

    def getValues(self) -> List[int]:
        curr = self.head.next
        out = []
        while curr:
            out.append(curr.val)
            curr = curr.next
        return out
