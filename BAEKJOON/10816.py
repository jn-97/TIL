# 숫자 카드 2
from sys import stdin

N = stdin.readline() # 상근이가 가지고 있는 카드 개수
s_list = list(map(int, stdin.readline().split())) # 카드에 적힌 수 N개
M = stdin.readline() # 찾아야 할 숫자 카드의 개수
n_list = list(map(int, stdin.readline().split())) # 찾아야 할 숫자

cnt = 0
result = []
for i in range(len(n_list)):
    for j in range(len(s_list)):
        if s_list[j] == n_list[i]:
            cnt += 1
    result.append(cnt)
    cnt = 0
        
print(*result)