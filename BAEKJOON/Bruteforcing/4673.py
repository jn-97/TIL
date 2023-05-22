# 셀프 넘버
import sys
input = sys.stdin.readline

n = set(range(1, 10001))
temp = set()

for i in range(1, 10001): # ex. i = 81 
    for j in str(i): # 81 + 8 => 89 + 1
        i += int(j)
    temp.add(i) # temp.add(90)

result = sorted(n-temp) # 기존 1부터 10000까지 숫자에서 셀프 넘버가 아닌 숫자들 빼기

for i in result:
    print(i)
