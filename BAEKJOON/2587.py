# 대표값2
import math

result = []
sum_ = 0
avg_ = 0

for _ in range(5):
    n = int(input())
    sum_ += n
    result.append(n)
avg_ = math.trunc(sum_/5) # 평균

result = sorted(result) # 정렬

print(avg_)
print(result[len(result)//2])