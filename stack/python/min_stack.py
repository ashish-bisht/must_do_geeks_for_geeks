class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self, val):
        if not self.stack:
            return "Nothing is there bro"
        self.stack.pop(0)

    def get_min(self):
        if not self.stack:
            return "Nothing there bro"

        return self.stack[0]


stack = MinStack()

stack.push(1)
stack.push(2)

print(stack.get_min())
