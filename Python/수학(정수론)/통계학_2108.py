from collections import Counter
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
result = list(map(int, data[1:N+1]))

# 산술평균 (반올림)
print(round(sum(result) / N))

# 중앙값
result.sort()
print(result[N // 2])

# 최빈값 (Counter 사용)
freq = Counter(result).most_common()
max_freq = freq[0][1]
modes = [num for num, count in freq if count == max_freq]
modes.sort()

# 최빈값 중 두 번째로 작은 값 출력
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

# 범위
print(max(result) - min(result))
