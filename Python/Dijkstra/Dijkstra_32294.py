import sys
from heapq import heappush, heappop

data = sys.stdin.read()
lines = data.splitlines()

n = int(lines[0])
a = list(map(int, lines[1].split()))
b = list(map(int, lines[2].split()))

result = []

for i in range(1, n + 1):
    if i - a[i-1] < 1 or i + a[i-1] > n:
        result.append(b[i-1])
    else:
        left = i
        left_cost = b[i-1]
        right = i
        right_cost = b[i-1]

        while True:
            left = left - a[left - 1]
            if left < 1:
                break
            left_cost += b[left - 1]

            right = right + a[right - 1]
            if right > n:
                break
            right_cost += b[right - 1]

        if left_cost < right_cost:
            result.append(left_cost)
        else:
            result.append(right_cost)

for i in result:
    print(i, end=" ")

# 모든 위치를 노드로 생각
# 수열 밖으로 나가는 위치(탈출 지점)를 도착 노드로 간주
# 각 위치에서 점프할 수 있는 곳으로 간선 (비용은 b[i])을 생성
# 다익스트라 알고리즘으로 각 위치에서 탈출 노드까지의 최단 시간 계산