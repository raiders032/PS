def push(x):
    if len(stack) == 0:
        stack.append(x)
    else:
        if x == '(':
            stack.append(x)
        elif x == ')':
            while stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()
        elif x == '*' or x == '/':
            while stack and stack[-1] != '(' and stack[-1] != '+' and stack[-1] != '-':
                print(stack.pop(), end='')
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.append(x)


string = input()
stack = []

for x in string:
    if x.isalpha():
        print(x, end='')
    else:
        push(x)
for i in range(len(stack)):
    print(stack.pop(), end='')
