import sys
string = list(sys.stdin.readline().strip())
cur = len(string)
N = int(sys.stdin.readline().strip())

for _ in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd.startswith('P'):
        cmd, ch = cmd.split()
        string.insert(cur, ch)
        cur += 1
    elif cmd.startswith('D'):
        cur += 1 if cur <= len(string) else 0
    elif cmd.startswith('L'):
        cur -= 1 if cur > 0 else 0
    elif cmd.startswith('B'):
        if cur == 0:
            continue
        string.pop(cur-1)
        cur -= 1
print(''.join(string))
