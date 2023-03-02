# 통나무 건너뛰기

import sys

sys.stdin = open("11497.txt")

# 첫 번째 풀이 (틀림 왜 틀렸는지 모르겠음)
# T = int(sys.stdin.readline())

# for tc in range(T):
#     N = int(sys.stdin.readline())
#     L = list(map(int, sys.stdin.readline().split()))

#     L.sort()

#     temp = []
#     for i in range(len(L)):  # i가 홀수면 일단 temp에 넣음
#         if (i % 2) != 0:
#             temp.append(L[i])

#     for t in temp:  # temp에 넣은 수를 리스트 L에서 제거
#         if t in L:
#             L.remove(t)

#     L.extend(temp[::-1])  # 리스트 L과 temp 합침

#     max_ = L[-1] - L[0]  # 첫번째 수와 마지막 수 더한 값을 max값으로 지정

#     for i in range(len(L) - 1):
#         if L[i + 1] - L[i] > max_:
#             max_ = L[i + 1] - L[i]

#     print(max_)

# 두 번째 풀이
import sys

T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    L = sorted(list(map(int, sys.stdin.readline().split())))
    cnt = []

    for i in range(N - 2):
        cnt.append(L[i + 2] - L[i])

    print(max(cnt))
