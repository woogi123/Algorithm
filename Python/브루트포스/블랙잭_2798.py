import sys
from heapq import heappush, heappop

data = sys.stdin.read()
lines = data.splitlines()

N, M = map(int, lines[0].split())

card = list(map(int, lines[1].split()))

card = sorted(card, reverse=True)

result = 0
for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            sum_check = card[i] + card[j] + card[k]
            if sum_check > result and sum_check <= M:
                result = sum_check
print(result)

# 3중 for문을 돌려도 되네..