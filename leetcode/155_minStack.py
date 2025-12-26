class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = min(self.getMin(), val) if len(self.stack) > 0 else val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# another approach is to use 2 stacks, one for storing values, one for storing min values. Since getMin only
# needs to return the min value corresponding with current stack state, we can just store the min value of each state
# of the stack along with a stack node
def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # return -3
    minStack.pop()
    print(minStack.top())  # return 0
    print(minStack.getMin())  # return -2


if __name__ == "__main__":
    main()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
