class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.arr = []
        self.curr_index = 0

        i = 0
        while i < len(v1) and i < len(v2):
            self.arr.append(v1[i])
            self.arr.append(v2[i])
            i += 1
        while i < len(v1):
            self.arr.append(v1[i])
            i += 1
        while i < len(v2):
            self.arr.append(v2[i])
            i += 1

    def next(self) -> int:
        out = self.arr[self.curr_index]
        self.curr_index += 1
        return out

    def hasNext(self) -> bool:
        return self.curr_index < len(self.arr)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
