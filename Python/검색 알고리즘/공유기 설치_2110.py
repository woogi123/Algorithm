import sys

input = sys.stdin.read
lines = input().strip().splitlines()

N, C = map(int, lines[0].split())

wifi = []
for i in range(1, N+1):
    wifi.append(int(lines[i]))

wifi.sort()

front = 1
rear = wifi[-1] - wifi[0]

while front <= rear:
    mid = (front + rear) // 2
    count = 1
    wifi_updated = wifi[0]
    for i in range(1, len(wifi)):
        if int(wifi[i]) - wifi_updated >=mid:
            count+=1
            wifi_updated = wifi[i]
    if count >= C:
        result = mid
        front = mid+1
    else:
        rear = mid-1



print(result)