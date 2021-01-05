string = input()
stack = []
for x in string:
    if x.isdigit():
        stack.append(int(x))
    if x == '+':
        stack.append(stack.pop() + stack.pop())
    elif x == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif x == '*':
        stack.append(stack.pop() * stack.pop())
    elif x == '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)
print(stack[-1])
