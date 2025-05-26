import sys
from collections import deque

m,n = map(int,sys.stdin.readline().rstrip().split())
a = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
dx, dy = [0,0,-1,1],[-1,1,0,0]

q = deque([])
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            q.append((i,j))
            
while q:
    cy,cx = q.popleft()
    for i in range(4):
        y = cy+dx[i]
        x = cx+dy[i]
        if 0 <= y < n and 0 <= x < m and a[y][x] == 0:
            a[y][x] = a[cy][cx] + 1
            q.append((y,x))

false = 0
t = False
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            false = 0
            t = True
            break
        false = max(false, a[i][j])
    if t : break

print(false-1)