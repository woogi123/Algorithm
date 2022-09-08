# 8 x 8 판에 퀸이 들어갈 경우의 수 구하기 (퀸이 서로 공격하는 방향에 있으면 안됨.)

# 규칙 찾기
# 1. 각 열에는 퀸이 하나씩 밖에 들어가지 못한다
# 2. 각 행에는 퀸이 하나씩 밖에 들어가지 못한다
# 3. 대각선에 퀸이 동시에 있으면 안된다.

# 보는법
# 8 X 8 블럭 (0,0), (2,4)에 퀸을 놓고 싶다 -> pos(0) = 0, pos(2) = 4


# 규칙 1
pos = [0] * 8

def put():          #배치한 퀸의 위치를 출력해주는 함수
  for i in range(8):
    print(f"{pos[i]:2}",end='')  # pos[i]:2 => 출력 시 2칸만큼 띄어쓰기 후 출력
    
def set(i):
  for j in range(8):
    pos[i] = j
    if i == 7:
      put()
    else:
      set(i+1)

set(0)

# 규칙 1 + 규칙 2
pos = [0] * 8
flag = [False] * 8

def put():
  for i in range(8):
    print(f"{pos[i]:2}",end='')

def set(i):
  for j in range(8):
    if not flag[j]:        # j행에 퀸이 없다면
      pos[i] = j
      if i == 7:
        put()
      else:
        flag[j] = True     # True -> flag[0]에 퀸을 설정했으므로 
        set(i+1)           # 다음 열로 넘어갈 때(set (i+1)) True 값을 갖고 넘어가려고 하기 위해서
        flag[j] = False

set(0)

# 규칙 1 + 2 + 3 (해답)
pos = [0] * 8
flag_a = [False] * 8  # 행
flag_b = [False] * 15 # 좌측상단에서부터 시작. / 대각선
flag_c = [False] * 15 # 좌측하단에서부터 시작. \ 대각선

def put():
  for i in range(8):
    print(f"{pos[i]:2}", end="")
  print()

def set(i):
  for j in range(8):
    if not flag_a[j] and not flag_b[i + j] and not flag_c[i + j - 7]:  # 행, 양 대각선에 퀸이 배치 X
      pos[i] = j
      if i == 7:
        put()
      else:
        flag_a[j] = flag_b[j] = flag_c[j] = True # 퀸 배치
        set(i+1)
        flag_a[j] = flag_b[j] = flag_c[j] = False

set(0)