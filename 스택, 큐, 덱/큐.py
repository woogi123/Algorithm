# 큐 함수

from typing import Any

class FixedQueue:
  class Empty(Exception):
    pass
  class Full(Exception):
    pass

  def __init__(self, capacity):
    self.capacity = capacity
    self.front = 0
    self.rear = 0
    self.no = 0
    self.que = [None] * self.capacity

  def is_empty(self):
    return self.no <= 0
  
  def is_full(self):
    return self.capacity <= self.no

  def enque(self,x):
    if self.is_full():
      raise FixedQueue.Full
    self.que[self.rear] = x
    self.no += 1
    self.rear += 1
    if self.rear == self.capacity:
      self.rear = 0
  
  def deque(self):
    if self.is_empty():
      raise FixedQueue.Empty
    x = self.que[self.front]
    self.no -= 1
    self.front += 1
    if self.front == self.capacity:
      self.front = 0
    return x

  def peek(self):
    if self.is_empty():
      raise FixedQueue.Empty
    return self.que[self.front]

  def find(self,value):
    for i in range(self.no):
      idx = self.que[i + self.front] % self.capacity # front부터 차례로 검사하기 때문에 i + self.front 이다.
      if self.que[idx] == value:
        return idx
    return -1

  def dump(self):
    if self.is_empty():
      print("큐에 값이 없습니다")
    else:
      for i in range(self.no):
        print(self.que[i + self.front] % self.capacity, end='')
      print()