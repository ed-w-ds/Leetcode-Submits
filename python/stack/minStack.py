class MinStack:

    def __init__(self):
        self.valueStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.valueStack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.valueStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.valueStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]   

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# second submit
class MinStack:

    def __init__(self):
        self.valueStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.valueStack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.valueStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.valueStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
