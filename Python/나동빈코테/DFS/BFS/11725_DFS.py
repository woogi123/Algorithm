import sys

# 재귀 깊이 제한을 늘려주는 코드 (but 이거 쓰면 보통 메모리오버남)
sys.setrecursionlimit(1000000)
# 재귀 <- 메모리 많이먹음 : 스택 사용

data = sys.stdin.read()
lines = data.splitlines()

# 좌표에서의 DFS
def dfs(x, y, visited, h):
    stack = [(x, y)]
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while stack:
        x, y = stack.pop()    

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                    if not visited[nx][ny] and check_map[nx][ny] > h:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

            # 재귀   
            # if nx >= 0 and nx < N and ny >= 0 and ny < N:
            #     if not visited[nx][ny] and check_map[nx][ny] > h:
            #         dfs(nx, ny, visited, h)

N = int(lines[0].strip())
result = []

check_map = []
for i in range(1, N + 1):
    check_map.append(list(map(int, lines[i].split())))


max_check = 0

for h in range(max(map(max, check_map)) + 1):
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if check_map[i][j] <= h:
                visited[i][j] = True

    result_list = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, visited, h)
                result_list += 1

    if result_list > max_check:     
        max_check = result_list

print(max_check)