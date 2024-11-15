class Stack:

    def __init__(self) -> None:
        self._stack = []

    def push(self, element):
        self._stack.append(element)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self._stack.pop()

    def getTop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self._stack[-1]

    def isEmpty(self):
        return len(self._stack) == 0
