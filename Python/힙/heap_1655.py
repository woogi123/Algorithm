import heapq
import sys

input = sys.stdin.readline
n = int(input())
max_heap = []
min_heap = []

for _ in range(n):
    num = int(input())
    heapq.heappush(max_heap, -num)

    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    # 균형 유지
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    print(-max_heap[0])
