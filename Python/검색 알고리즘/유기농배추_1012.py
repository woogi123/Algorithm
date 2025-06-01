import sys

data = sys.stdin.read()
lines = data.splitlines()

case = int(lines[0])


def bfs(cabbage_x, cabbage_y):
    q = []
    q.append((cabbage_x, cabbage_y))
    visited[cabbage_y][cabbage_x] = True

    direction = [(-1, 0), (1, 0), (0, -1), (0,1)]    
    # 상하좌우

    while q:
        x, y = q.pop(0)

        for dx, dy in direction:
            x_1, y_1 = x + dx, y + dy
            # 상하좌우 배추 확인
            if 0 <= x_1 < n and 0 <= y_1 < m:
                # x_1, y_1이 배추밭 사이에 있는 값인지 체크
                if result[y_1][x_1] and not visited[y_1][x_1]:
                    # 배추가 있고, 방문하지 않은 좌표이면 q에 추가
                    visited[y_1][x_1] = True
                    q.append((x_1, y_1))


idx = 1
for _ in range(case):
    n, m, cabbage = map(int, lines[idx].split())

    # 배추밭 만들기
    result = [[False] *  n for _ in range(m)]
    visited = [[False] * n for _ in range(m)] # 2차원 배열이기 때문에 visited도 2차원으로
    idx += 1

    # 배추 심기
    for i in range(cabbage):
        cabbage_x, cabbage_y = map(int, lines[idx].split())

        result[cabbage_y][cabbage_x] = True
        idx += 1
        # why (y, x)로 저장하는가?
        # -> x: 열, y: 행 이기 때문에 
        # (x, y)로 저장한다면 visited[1][2] 는
        # [0, 0, 0, 0, 0]
        # [0, 0, 1, 0, 0]  이렇게 저장된다.
        # [0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0]

        # (y, x)로 저장한다면 visited[2][1] 는
        # [0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0]  이렇게 저장된다. 따라서 행, 열을 고려하여 y, x를 바꿔야한다.
        # [0, 1, 0, 0, 0]
        # [0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0]


    # 배추 집합 개수세기
    worm = 0
    for y in range(m):
        for x in range(n):
            if result[y][x] == True and not visited[y][x]:
                # 배추가 있고, 방문하지 않았다면
                bfs(x, y)
                worm +=1
    print(worm)
