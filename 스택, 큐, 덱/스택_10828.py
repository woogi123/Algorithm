# 스택 함수

from typing import Any

class FixedStack:

  class Empty(Exception):      #Exception : 어떤 오류던지 발생 시 아래 내용을 수행
    pass
  class Full(Exception):
    pass

  def __init__(self, capacity : int = 256) -> None:
   self.capacity = capacity
   self.stk = [None] * self.capacity
   self.ptr = 0
  
  def __len__(self):
    return self.ptr
  
  def is_empty(self):
    return self.ptr <= 0
  def is_full(self):
    return self.ptr >= self.capacity
  
  def push(self, value):
    if self.is_full():
      raise FixedStack.Full
    self.stk[self.ptr] = value
    self.ptr += 1

  def pop(self):
    if self.is_empty():
      raise FixedStack.Empty
    self.ptr -= 1
    return self.stk[self.ptr]

  def peek(self):
    if self.is_empty():
      raise FixedStack.Empty
    return self.stk[self.ptr - 1]

  def clear(self):
    self.ptr = 0

  def find(self,value):
    if self.is_empty():
      raise FixedStack.Empty
    for i in range(self.ptr - 1,-1,-1):
      if self.stk[i] == value:
        return i
    return -1

  def count(self,value):
    c = 0
    for i in range(self.ptr):
      if self.stk[i] == value:
        c += 1
    return c

  def __contain__(self,value):
    return self.count(value) > 0
  
  def dump(self):
    if self.is_empty():
      print("스택이 비었습니다")
    else:
      print(self.stk[:self.ptr])

# 스택 구현