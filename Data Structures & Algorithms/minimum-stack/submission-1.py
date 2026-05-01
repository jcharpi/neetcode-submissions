class MinStack:
    #set min = inf
    # if value < minStack top element, add to minStack
    # add 1, don't add 2, add, 0
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(not self.minStack or val <= self.minStack[-1]):
            self.minStack.append(val)

    def pop(self) -> None:
        popVal = self.stack.pop()
        if(popVal == self.minStack[-1]):
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
# -2, -2, 
# -2, 