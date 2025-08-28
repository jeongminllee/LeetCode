class MinStack:
    def __init__(self):
        self.minstack = []

    def push(self, val: int) -> None:
        currMin = self.getMin()
        if val < currMin :
            currMin = val
        
        self.minstack.append((val, currMin))

    def pop(self) -> None:
        self.minstack.pop()

    def top(self) -> int:
        return self.minstack[-1][0]

    def getMin(self) -> int:
        if not self.minstack :
            return float('inf')

        return self.minstack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()