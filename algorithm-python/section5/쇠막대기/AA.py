string = list(input())
stack = []
cur = 0
res = 0
i = 0
while i < len(string):
    if string[i] == '(' and string[i+1] == ')':
        i += 1
        res += len(stack)
    elif string[i] == '(':
        stack.append('(')
    elif string[i] == ')':
        stack.pop()
        res += 1
    i += 1
print(res)
