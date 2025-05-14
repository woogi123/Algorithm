import sys

input = sys.stdin.read
lines = input().strip().splitlines()

n = int(lines[0])
lst = list(map(int, lines[1].split()))

stack = []
result = []

check = 0
for i in range(len(lst) - 1, -1, -1):
    if len(stack) == 0:
        stack.append(lst[i])
        result.append(-1)

    elif stack[-1] > lst[i]:
        result.append(stack[-1])
        stack.append(lst[i])
    else:
        while stack[-1] <= lst[i]:
            stack.pop()
            if len(stack) == 0:
                stack.append(lst[i])
                result.append(-1)
                check = 1
                break
        if check != 1:
            result.append(stack[-1])
            stack.append(lst[i])
        check = 0

print(*result[::-1])
