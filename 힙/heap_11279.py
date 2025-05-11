import sys
import heapq

input = sys.stdin.read
lines = input().strip().splitlines()

N = int(lines[0])
result = []
for i in range(1, N+1):
  if int(lines[i]) == 0:
    if len(result) == 0:
      print(0)
    else:
      num = -heapq.heappop(result)
      print(num)
  else:
    heapq.heappush(result, -int(lines[i]))

