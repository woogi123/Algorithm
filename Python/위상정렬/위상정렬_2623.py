from collections import deque
import sys

data = sys.stdin.read()
lines = data.splitlines()

N, M = map(int, lines[0].split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for i in range(1, M + 1):
    lists = list(map(int, lines[i].split()))
    num = lists[0]
    for j in range(1,num):
        graph[lists[j]].append(lists[j+1])
        indegree[lists[j+1]] += 1

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

while len(indegree) != 0:
    check = indegree.pop()
    if check != 0:
        print(0)
        break
    
if len(indegree) == 0:
    for i in result:
        print(i)

