import sys
from collections import deque

def add(s, e):
    a[s].append(e)
    a[e].append(s)

def bfs(st):
    q = deque()
    q.append(st)
    v[st] = 1

    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for next in a[cur]:
            if v[next] == 1:
                continue
            v[next] = 1
            q.append(next)

def dfs(cur):
    v[cur] = 1
    print(cur, end=' ')
    for next in a[cur]:
        if v[next] == 0:
            dfs(next)

lines = sys.stdin.readlines()
N, M, V = map(int, lines[0].split())

a = [[] for _ in range(N + 1)]
v = [0] * (N + 1)

for i in range(1, M + 1):
    s, e = map(int, lines[i].split())
    add(s, e)

for i in range(1, N + 1):
    a[i].sort()
dfs(V)
print()

v = [0] * (N + 1)

bfs(V)
