import sys

data = sys.stdin.read()
lines = data.splitlines()

def dfs(x, y, graph, visited):
    stack = [(x, y)]
    visited[x][y] = True
    color = graph[x][y]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == color:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

N = int(lines[0])

check_map = []
for i in range(N):
    check_map.append(list(lines[i + 1].strip()))


blind_map = []
for row in check_map:
    blind_map.append(['G' if x == 'R' else x for x in row])

visited1 = [[False] * N for _ in range(N)]
count1 = 0

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            dfs(i, j, check_map, visited1)
            count1 += 1

visited2 = [[False] * N for _ in range(N)]
count2 = 0

for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            dfs(i, j, blind_map, visited2)
            count2 += 1

print(count1, count2)