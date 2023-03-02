# 보석 도둑

import sys, heapq

sys.stdin = open("1202.txt")

# 첫 번째 풀이 : 런타임 에러
# N, K = map(int, sys.stdin.readline().split())  # 보석, 가방

# MV_list = []
# for _ in range(N):  # 보석 개수 만큼
#     MV = list(map(int, sys.stdin.readline().split()))
#     MV_list.append(MV)

# C_list = []
# for _ in range(K):
#     C = int(sys.stdin.readline())
#     C_list.append(C)

# C_list.sort()

# result = []
# sum_ = 0
# for i in range(len(C_list)):
#     for j in range(len(MV_list)):
#         if C_list[i] >= MV_list[j][0]:
#             result.append(MV_list[j][1])

#     sum_ += max(result)
#     for k in range(len(MV_list)):
#         if max(result) == MV_list[k][1]:
#             MV_list.remove(MV_list[k])
#             break
#     result = []

# print(sum_)

# 두 번째 풀이
N, K = map(int, sys.stdin.readline().split())  # 보석, 가방

MV_list = []
for _ in range(N):  # 보석 개수 만큼
    M, V = map(int, sys.stdin.readline().split())
    MV_list.append((M, V))

C_list = []
for _ in range(K):
    C = int(sys.stdin.readline())
    C_list.append(C)

MV_list.sort()
C_list.sort()

ans = 0
idx = 0
poss = []

for c in C_list:  # C_list 가장 작은 가방부터 확인
    while idx < N:
        M, V = MV_list[idx]
        if M <= c:  # 보석의 무게가 가방 무게보다 적으면
            heapq.heappush(poss, -V)
            idx += 1
        else:
            break

    if poss:
        ans += -heapq.heappop(poss)  # 가방에 넣을 수 있는 보석 중 가장 가치가 높은 보석 더해주기

print(ans)
