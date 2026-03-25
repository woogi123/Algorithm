import sys
from collections import deque

data = sys.stdin.read()
lines = data.splitlines()


def bfs(x, y):
    queue = deque([(x, y)])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if check_map[nx][ny] == 1:
                    check_map[nx][ny] = check_map[x][y] + 1
                    queue.append((nx, ny))

N, M = map(int, lines[0].split())

check_map = []
for i in range(N):
    check_map.append(list(map(int, lines[i + 1].strip())))


bfs(0, 0)
print(check_map[N - 1][M - 1])