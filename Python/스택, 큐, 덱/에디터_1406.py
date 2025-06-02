import sys

data = sys.stdin.read().strip()
lines = data.splitlines()

line = lines[0]
M = int(lines[1])
commands = lines[2:]

left_list = list(line)
right_list = []


for i in range(M):
    if commands[i][0] == 'L':
        if len(left_list) != 0:
            right_list.append(left_list.pop())

    elif commands[i][0] == 'D':
        if len(right_list) != 0:
            left_list.append(right_list.pop())

    elif commands[i][0] == 'B':
        if len(left_list) != 0:
            left_list.pop()
    elif commands[i][0] == 'P':
        left_list.append(commands[i][2])

print(''.join(left_list + right_list[::-1]))