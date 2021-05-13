class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return not self.stack or False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return None if self.isEmpty() else self.stack.pop()

    def peek(self):
        return None if self.isEmpty() else self.stack[-1]

    def size(self):
        return len(self.stack)
