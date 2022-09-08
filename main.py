def quick_sort(x):
  n = len(x)
  pl = 0
  pr = n-1
  pc = x[n//2]       # 미리 설정해놔야함 ? 왜
  while pl < pr:          
    while x[pl] < pc:
      pl += 1 
    while x[pr] > pc:
      pr -= 1
    if pl <= pr:                        
      x[pl], x[pr] = x[pr], x[pl]
      pl += 1
      pr -= 1
  print("피벗: ", pc)
  print(x[0:pl])
  print(x[pr+1:n])

x = [475,623,472,57,45,73,568,346,24362,488,46,345,123,423,6693,23523,223,4123,132]
quick_sort(x)