# 통계학
import sys
from collections import Counter

sys.stdin = open("2108.txt")

T = int(sys.stdin.readline())

n_list = []
for tc in range(T):
    n_list.append(int(sys.stdin.readline()))

n_list.sort()
max_n_list = Counter(n_list).most_common()

print(round(sum(n_list) / T))  # 산술평균

print(n_list[T // 2])  # 중앙값

if len(max_n_list) > 1:  # 최빈값
    if max_n_list[0][1] == max_n_list[1][1]:
        print(max_n_list[1][0])
    else:
        print(max_n_list[0][0])
else:
    print(max_n_list[0][0])

print(n_list[-1] - n_list[0])  # 최댓값과 최솟값의 차이
