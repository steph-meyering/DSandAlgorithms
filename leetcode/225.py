class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.t = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        self.t = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        tmp = deque()
        for i, el in enumerate(self.q):
            if i == len(self.q) - 2:
                self.t = el
            if i == len(self.q) - 1:
                self.q = tmp
                return el
            tmp.append(el)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.t

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
