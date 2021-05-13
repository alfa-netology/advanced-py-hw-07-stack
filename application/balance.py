from application.cls_stack import Stack

PAIRS_OF_BRACKETS = ('()', '[]', '{}')

stack = Stack()

def check(string):
    for char in string:
        if char in '([{':
            stack.push(char)
        else:
            if stack.isEmpty():
                return False
            else:
                if stack.peek() + char in PAIRS_OF_BRACKETS:
                    stack.pop()
                else:
                    return False

    return stack.isEmpty() or False
