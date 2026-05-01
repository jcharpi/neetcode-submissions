class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        # 1, 2, 0
        # 1, 0
    def pop(self) -> None:
        valToPop = self.stack.pop()
        if self.minStack[-1] == valToPop:
            self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
