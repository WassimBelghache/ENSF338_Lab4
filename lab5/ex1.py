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

if len(sys.argv) != 2:
    sys.exit(1)

operations_list = ['+','-','*','/']
expression = sys.argv[1]

stack = Stack()
for char in expression:
    if char == '(':
        continue
    elif char in operations_list:
        stack.push(char)
    elif char.isdigit():
        stack.push(char)
    elif char == ')':
        num2 = stack.pop()
        num1 = stack.pop()
        operation = stack.pop()
        new_expression = str(num1) + ' ' + operation + ' ' + str(num2)
        calculate = int(eval(new_expression))
        stack.push(calculate) 


print("Result:", stack.pop())