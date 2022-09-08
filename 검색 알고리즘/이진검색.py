#2. 이진검색
# 배열이 규칙적일때 사용시 시간단축

from typing import Any, Sequence

def bin_search(x : Sequence, key : Any) -> int:
  pl = 0
  pr = len(x) - 1
  while True:
    pc = (pl + pr) // 2
    if x[pc] == key:
      return pc
    elif x[pc] > key:
      pr = pc - 1
    elif x[pc] < key:
      pl = pc + 1

    if pl > pr:
      break
  return -1

if __name__ == "__main__":
  x_len = int(input("원소 수를 입력해주세요: "))
  x = x_len * [None]
  
  x[0] = int(input("x[0] = "))
  for i in range(1,x_len):
    x[i] = int(input(f"x[{i}] = "))
    if x[i-1] >= x[i]:
      print("배열의 규칙이 불규칙합니다")
      break

  key = int(input("원하는 값을 입력하세요: "))

  idx = bin_search(x, key)

  if idx == -1:
    print("검색 실패")
  else:
    print(f"찾고자 하는 값은 x[{idx}] 에 있습니다")