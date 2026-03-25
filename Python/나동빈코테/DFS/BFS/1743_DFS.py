import sys

data = sys.stdin.read()
lines = data.splitlines()

def dfs(x, y, visited):
    stack = [(x, y)]
    visited[x][y] = True


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    num = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and check_map[nx][ny] == 1:
                    num += 1
                    visited[nx][ny] = True
                    stack.append((nx, ny))
    return num

N, M, K = map(int, lines[0].split())

check_map = [[0] * M for i in range(N)]
for i in range(K):
    a, b = map(int, lines[i+1].split())
    check_map[a-1][b-1] = 1

max_num = 0
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not visited[i][j] and check_map[i][j] == 1:
            num = dfs(i, j, visited)
            if max_num < num:
                max_num = num


print(max_num)