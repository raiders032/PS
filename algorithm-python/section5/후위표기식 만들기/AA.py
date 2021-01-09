def push(x):
    if x == '(':
        stack.append(x)
    elif stack:
        if x == ')':
            while stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.append(x)
        elif x == '*' or x == '/':
            while stack[-1] != '(' and (stack[-1] == '*' or stack[-1] == '/'):
                print(stack.pop(), end='')
            stack.append(x)
    else:
        stack.append(x)


stack = []
string = input()

for x in string:
    if x.isdigit():
        print(x, end='')
    else:
        push(x)

for i in range(len(stack)):
    print(stack.pop(), end='')
