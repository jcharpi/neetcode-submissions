class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        queue2 = [x]

        while self.queue:
            queue2.append(self.queue.pop(0))
        
        self.queue = queue2
        queue2 = []
        

    def pop(self) -> int:
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()