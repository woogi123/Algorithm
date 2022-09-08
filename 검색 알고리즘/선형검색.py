# 1. 선형검색
from typing import Any, Sequence

def seq_search(a : Sequence, key : Any) -> int:
  i = 0

  while True:
    if x[i] == key:
      return i
    elif x[i] == len(x):
      return -1
    i += 1

if __name__ == "__main__":
  x_len = int(input("원소 수를 입력해주세요: "))
  x = x_len * [None]
  for i in range(x_len):
    x[i] = int(input(f"x[{i}] = "))

  key = int(input("검색할 값을 입력해주세요: "))

  idx = seq_search(x, key)

  if idx == '-1':
    print("검색 실패")
  else:
    print(f"찾고자 하는 값은 x[{idx}] 에 있습니다.")
    