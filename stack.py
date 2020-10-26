class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


balanced = '((()))'
unbalanced = '(()'

def check_balance(parenthesis_string: str) -> bool:
    stack = Stack()
    is_balanced = True
    for pointer in range(len(parenthesis_string)):
        if parenthesis_string[pointer] in '([{':
            stack.push(parenthesis_string[pointer])
        else:
            if stack.isEmpty():
                is_balanced = False
            else:
                top = stack.pop()
                if not matches(open_symbol=top, close_symbol=parenthesis_string[pointer]):
                    is_balanced = False
    if stack.isEmpty() and is_balanced:
        return True
    else:
        return False


def matches(open_symbol, close_symbol):
    if open_symbol == '(':
        if close_symbol == ')':
            return True
    if open_symbol == '[':
        if close_symbol == ']':
            return True
    if open_symbol == '{':
        if close_symbol == '}':
            return True
    return False

multi_balanced = '{({([][])}())}'
multi_unbalanced = '[{()]'

print(check_balance(multi_unbalanced))
