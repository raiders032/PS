"""
https://www.acmicpc.net/problem/1935
1935.후위 표기식2
실버3
풀이1.72ms
"""
N = int(input())
exp = input()
num = [0] * N
for i in range(N):
    num[i] = int(input())

stack = []

for ch in exp:
    if ch.isalpha():
        stack.append(num[ord(ch) - ord('A')])
    else:
        if ch == "+":
            stack.append(stack.pop() + stack.pop())
        elif ch == "*":
            stack.append(stack.pop() * stack.pop())
        elif ch == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)

print(f'{stack[-1]:.2f}')