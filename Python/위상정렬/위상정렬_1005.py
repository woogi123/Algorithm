from collections import deque
import sys

data = sys.stdin.read()
lines = data.splitlines()

T = int(lines[0])
t = 1

for case in range(T):
    N, K = map(int, lines[t].split())
    t += 1

    time = list(map(int, lines[t].split()))
    t += 1

    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, lines[t].split())
        graph[X].append(Y)
        indegree[Y] += 1
        t += 1

    W = int(lines[t])
    t += 1

    q = deque()
    result = [0] * (N + 1)

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = time[i - 1]

    while q:
        num = q.popleft()
        for next in graph[num]:
            indegree[next] -= 1
            result[next] = max(result[next], result[num] + time[next - 1])
            if indegree[next] == 0:
                q.append(next)

    print(result[W])

# 위상정렬 + DP로 풀어야함.
