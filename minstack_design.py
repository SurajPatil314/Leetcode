"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.min = None

    def push(self, x: int) -> None:
        self.st.append(x)
        if self.min == None:
            self.min = x
        else:
            self.min = min(self.min, x)

    def pop(self) -> None:
        if len(self.st) > 0:
            del self.st[-1]
            if len(self.st) == 0:
                self.min = None
            else:
                self.min = min(self.st)

    def top(self) -> int:
        if len(self.st) > 0:
            return self.st[len(self.st) - 1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.st) > 0:
            return self.min
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()