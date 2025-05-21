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

q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

result = []

while q:
    num = q.popleft()
    result.append(num)
    for next in graph[num]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

for i in result:
    print(i, end=" ")

# 위상정렬: 간선의 방향 순서대로 정점을 나열함.
# indegree가 0인 것을 먼저 queue에 넣는방식
# 파이썬은 라이브러리를 지원해줌 (from graphlib import TopologicalSorter)
