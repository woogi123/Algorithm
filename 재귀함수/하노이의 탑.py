#재귀적 표현
def hanoi(no,x,y): # no =  옮겨야 할 원반 수, x : 시작기둥, y : 끝기둥
  if no > 1:
    hanoi(no - 1 , x , 6-x-y)  # 처음 -> 중간
  print(f"원반[{no}]를 {x}기둥에서 {y}기둥으로 옮깁니다.")

  if no > 1:
    hanoi(no - 1, 6-x-y, y)    # 중간 -> 끝 

x = int(input("원판 수: "))
print(hanoi(x,1,3))


# 원판이 3개 일때
# hanoi (3,1,3)     앞 if문
#   hanoi (2,1,2)
#     hanoi (1,1,3)
#     hanoi (1,3,2)
#   hanoi (2,2,3)   뒤 if 문
#     hanoi (1,2,1)
#     hanoi (1,1,3)


#비재귀적 표현
def move(x, y):
  print(f"{x} -> {y}")

def hanoi(no):
  s = FixedStack() # 스택 사용
  x = "1"
  y = "3"
  z = "2"
  while True:
    while no > 1:
      s.push(y)
      s.push(z)
      s.push(x)
      s.push(no)

      no -= 1
      z, y = y, z # 중간, 끝 교환

    move(x,y)

    if s.is_empty() == False:
      no = s.pop()
      x = s.pop()
      z = s.pop()
      y = s.pop()

      move(x,y)
      no -=1
      x,z = z,x # 처음, 중간 교환
    else:
      break

x = int(input("원판 갯수: "))
print(hanoi(x))