import sys
left = list(sys.stdin.readline().strip())
right = []
N = int(sys.stdin.readline().strip())

for _ in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd.startswith('P'):
        cmd, ch = cmd.split()
        left.append(ch)
    elif cmd.startswith('L'):
        if left:
            right.append(left.pop())
    elif cmd.startswith('D'):
        if right:
            left.append(right.pop())
    elif cmd.startswith('B'):
        if left:
            left.pop()
print(''.join(left + right[::-1]))
