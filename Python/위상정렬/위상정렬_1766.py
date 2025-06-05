from collections import deque
import sys

data = sys.stdin.read()
lines = data.splitlines()

N, M = map(int, lines[0].split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for i in range(1, M + 1):
    a, b = map(int, lines[i].split())
    graph[a].append(b)
    indegree[b] += 1

q = []

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

result = []

while q:
    q.sort()
    num = q.pop(0)
    result.append(num)
    for next in graph[num]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

for i in result:
    print(i, end=" ")
