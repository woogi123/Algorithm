import sys

sys.setrecursionlimit(10000)

data = sys.stdin.read()
lines = data.splitlines()

def dfs(x, y, visited):
    stack = [(x, y)]
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if not visited[nx][ny] and check_map[nx][ny] != 'X':
                    visited[nx][ny] = True
                    result.append(check_map[nx][ny])
                    stack.append((nx, ny))

N, M = map(int, lines[0].split())

check_map = []
for i in range(1, N + 1):
    #strip: 1문자씩, split: 입력 자체로
    check_map.append(list(map(str, lines[i].strip())))

for i in range(N):
    for j in range(M):
        if check_map[i][j] == 'I':
            I_x, I_y = i, j
            break

visited = [[False] * M for _ in range(N)]
result = []
dfs(I_x, I_y, visited)

num = 0
for i in result:
    if i == 'P':
        num += 1

if num == 0:
    print('TT')
else:
    print(num)