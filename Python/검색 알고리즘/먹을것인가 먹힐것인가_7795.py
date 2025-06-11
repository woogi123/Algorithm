import sys
from bisect import bisect_left

lines = sys.stdin.readlines()

idx = 0
case = int(lines[idx])

for _ in range(case):
    idx += 1
    n, m = map(int, lines[idx].split())

    idx += 1
    A = list(map(int, lines[idx].split()))

    idx += 1
    B = list(map(int, lines[idx].split()))

    B.sort()

    count = 0
    for a in A:

        count += bisect_left(B, a)

    print(count)
