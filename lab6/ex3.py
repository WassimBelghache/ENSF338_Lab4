import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(expression):
    tokens = expression.split()
    stack = []
    for token in tokens:
        if token.isdigit():
            node = Node(token)
            stack.append(node)
        elif token in {'+', '-', '*', '/'}:
            if len(stack) < 2:
                print("Error: Insufficient operands for operator:", token)
                return None
            right_operand = stack.pop()
            left_operand = stack.pop()
            node = Node(token)
            node.right = right_operand
            node.left = left_operand
            stack.append(node)
        else:
            print("Error: Unexpected token encountered:", token)
            return None
    if len(stack) != 1:
        print("Error: Malformed expression")
        return None
    return stack.pop()

def evaluate_tree(root):
    if root.value.isdigit():
        return int(root.value)
    left_val = evaluate_tree(root.left)
    right_val = evaluate_tree(root.right)
    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        if right_val == 0:
            print("Error: Division by zero")
            return None
        return left_val / right_val

def main():
    if len(sys.argv) != 2:
        print("Usage: python ex3.py \"expression\"")
        return

    expression = sys.argv[1]
    root = build_tree(expression)
    if root is None:
        print("Error: Unable to parse the expression.")
        return

    result = evaluate_tree(root)
    if result is not None:
        print(result)

if __name__ == "__main__":
    main()