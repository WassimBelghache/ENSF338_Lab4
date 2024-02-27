import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def evaluate_expression(expression):
    stack = Stack()
    tokens = expression.split()
    
    for token in tokens:
        if token == '(':
            continue
        elif token.isdigit():
            stack.push(int(token))
        elif token in ['+', '-', '*', '/']:
            stack.push(token)
        elif token == ')':
            operand = stack.pop()
            e2 = stack.pop()
            e1 = stack.pop()
            result = apply_operation(e1, e2, operand)
            stack.push(result)

    return stack.pop()

def apply_operation(e1, e2, operand):
    if operand == '+':
        return e1 + e2
    elif operand == '-':
        return e1 - e2
    elif operand == '*':
        return e1 * e2
    elif operand == '/':
        return e1 / e2

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex1.py '<expression>'")
        sys.exit(1)

    expression = sys.argv[1]
    result = evaluate_expression(expression)
    print(result)
