import sys
from collections import deque

data = sys.stdin.read()
lines = data.splitlines()

M, N, H = map(int, lines[0].split())

check_map = []
queue = deque()

idx = 1
for h in range(H):
    floor = []
    for x in range(N):
        row = list(map(int, lines[idx].split()))
        floor.append(row)

        for y in range(M):
            if row[y] == 1:
                queue.append((h, x, y))
        idx += 1
    check_map.append(floor)

def bfs():
    dh = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]

    while queue:
        h, x, y = queue.popleft()

        for i in range(6):
            nh = h + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M:
                if check_map[nh][nx][ny] == 0:
                    check_map[nh][nx][ny] = check_map[h][x][y] + 1
                    queue.append((nh, nx, ny))

bfs()

answer = 0
for h in range(H):
    for x in range(N):
        for y in range(M):
            if check_map[h][x][y] == 0:
                print(-1)
                sys.exit()
            if answer < check_map[h][x][y]:
                answer = check_map[h][x][y]

print(answer - 1)