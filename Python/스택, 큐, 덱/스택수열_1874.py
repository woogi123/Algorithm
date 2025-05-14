import sys
from collections import deque

input = sys.stdin.read
lines = input().strip().splitlines()

n = int(lines[0])
result = deque(map(int, lines[1:]))

stack = []
stack_set = set()
i = 1
operations = []

while result:
    if i <= n and (not stack or stack[-1] < result[0]):
        stack.append(i)
        stack_set.add(i)
        operations.append('+')
        i += 1
    elif stack and stack[-1] == result[0]:
        stack_set.remove(stack.pop())
        result.popleft()
        operations.append('-')
    else:
        print('NO')
        sys.exit(0)

print('\n'.join(operations))