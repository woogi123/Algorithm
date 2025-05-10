import sys

input = sys.stdin.read
lines = input().strip().splitlines()

N, M, L = map(int, lines[0].split())

rest_house = list(map(int, lines[1].split())) if N > 0 else []

rest_house = [0] + sorted(rest_house) + [L]

front = 1
rear = L

while front <= rear:

    mid = (front + rear) // 2
    count = 0
    for i in range(1, len(rest_house)):
        num = rest_house[i] - rest_house[i-1]
        count += num // mid
        if num % mid == 0:
            count -=1
        
    if count <= M:
        rear = mid-1
    else:
        front = mid+1

print(front)