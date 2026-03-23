import sys

data = sys.stdin.read().strip().splitlines()

N = int(data[0])
N_lines = [tuple(map(int, line.split())) for line in data[1:]]

N_lines.sort(key=lambda x: (x[1], x[0]))

count = 0
last = 0

for i in N_lines:
    if i[0] >= last:
        last = i[1]
        count += 1

print(count)