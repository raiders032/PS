def evl(string):
    stack = []
    for x in string:
        if x.isalpha():
            stack.append(arr[ord(x) - ord('A')])
        else:
            if x == "+":
                stack.append(stack.pop() + stack.pop())
            elif x == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif x == "*":
                stack.append(stack.pop() * stack.pop())
            elif x == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(a/b)
    return stack.pop()


N = int(input())
string = input()
arr = []
for i in range(N):
    arr.append(float(input()))
print('%.2f' % evl(string))
