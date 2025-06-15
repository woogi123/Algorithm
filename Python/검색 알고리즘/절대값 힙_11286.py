import sys
import heapq

input = sys.stdin.read
lines = input().strip().splitlines()

N = int(lines[0])

hip_p = []
hip_m = []
for i in range(N):
    a = int(lines[i+1])
    if a == 0:
        if len(hip_p) == 0 and len(hip_m) == 0:
            print('0')
        elif len(hip_p) == 0:
            abs_m = heapq.heappop(hip_m)            
            print(-abs_m)
        elif len(hip_m) == 0:
            abs_p = heapq.heappop(hip_p)
            print(abs_p)
        else:
            abs_p = heapq.heappop(hip_p)
            abs_m = heapq.heappop(hip_m)

            if abs_p >= abs_m:
                print(-abs_m)
                heapq.heappush(hip_p, abs(abs_p))
            else:
                print(abs_p)
                heapq.heappush(hip_m, abs(abs_m))
    else:
        if a > 0:
            heapq.heappush(hip_p, abs(a))
        if a < 0:
            heapq.heappush(hip_m, abs(a))