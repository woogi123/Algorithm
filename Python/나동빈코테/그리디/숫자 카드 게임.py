import sys

data = sys.stdin.read()
lines = data.splitlines()

M, N = map(int, lines[0].split())

min_list = []
for i in range(M):
    min_list.append(min(list(map(int, lines[i+1].split()))))

print(max(min_list))