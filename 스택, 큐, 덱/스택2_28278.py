import sys

data = sys.stdin.read()
lines = data.splitlines()

def stack(n, result):
    if n[0] == '1':
        result.append(int(n[1]))
    elif n[0] == '2':
        print(result.pop() if result else -1)
    elif n[0] == '3':
        print(len(result))
    elif n[0] == '4':
        print(1 if not result else 0)
    elif n[0] == '5':
        print(result[-1] if result else -1)

N = int(lines[0])
result = []
for i in range(1, N+1):
    n = lines[i].split()
    stack(n, result)
