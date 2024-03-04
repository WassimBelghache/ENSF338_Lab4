class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def evaluate_expression(expression):
    stack = Stack()
    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        elif token in ['+', '-', '*', '/']:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operation(token, operand1, operand2)
            stack.push(result)
        elif token == '(':
            pass
        elif token == ')':
            pass
    return stack.pop()

def apply_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python ex1.py 'expression'")
        sys.exit(1)
    expression = sys.argv[1]
    result = evaluate_expression(expression)
    print(result)
