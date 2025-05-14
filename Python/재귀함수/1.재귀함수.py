# 재귀함수 : 함수 내에서 함수를 또 쓰는 것
# 함수를 여러번 돌려야 해서 속도가 느려지지만, 가독성이 좋음
# 코드 보관 등에 용이함


# 비재귀적 풀이
import FixedStack

def recur(n):
  s = FixedStack(n)

  while True:

    if n > 0:
      s.push(n) # 4, 3, 2, 1 스택에 푸시 -> 
                # 이후 3-2=1에서 나온 값 푸시 -> 이후 2 푸시 -> 1푸시
      n = n-1
      continue # while문 처음으로 돌아감
    # n이 0이 되면 실행
    if not s.is_empty():
      n = s.pop() # 1, 2, 3 팝 이후 1 팝 -> 4팝 -> 1팝 -> 2팝
      print(n) 
      n = n-2 # 3 - 2 = 1이므로 다시 if n>0문 실행됨
              # 따라서 4 팝 안됨
      continue

    break

x = int(input("값: "))
print(recur(x))

# 재귀적 풀이
def recur(n):
  if n > 0:
    recur(n-1)
    print(n)
    recur(n-2)

x = int(input("값: "))
print(recur(x))