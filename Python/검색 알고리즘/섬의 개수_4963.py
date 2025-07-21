import sys
from collections import deque

data = sys.stdin.read().strip()
lines = data.splitlines()

a = 0

def bfs(x, y):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    q = deque()
    q.append((x, y))
    visited[y][x] = True

    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            check_x, check_y = x + dx, y + dy
            if 0 <= check_x < w and 0 <= check_y < h and not visited[check_y][check_x] and int(land_map[check_y][check_x]) == 1:
                visited[check_y][check_x] = True
                q.append((check_x, check_y))

while True:
    w, h = map(int, lines[a].split())
    a += 1
    if w == 0 and h == 0:
        break

    land_map = [lines[i + a].split() for i in range(h)]
    visited = [[False] * w for _ in range(h)]
    a += h

    land_count = 0
    for y in range(h):
        for x in range(w):
            if int(land_map[y][x]) == 1 and not visited[y][x]:
                bfs(x, y)
                land_count += 1
    print(land_count)
