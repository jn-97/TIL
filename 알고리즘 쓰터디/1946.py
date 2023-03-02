# 신입 사원

import sys

sys.stdin = open("1946.txt")

T = int(sys.stdin.readline())

# 시간 초과 (이중반복문)
# for tc in range(T):
#     N = int(sys.stdin.readline())

#     list_ = []
#     for n in range(N):
#         st_1, st_2 = map(int, sys.stdin.readline().split())
#         list_.append((st_1, st_2))

#     list_.sort()

#     cnt = 0
#     v = list_[0][1]
#     for i in range(len(list_)):
#         for j in range(1, len(list_)):
#             if list_[j][1] < v:
#                 cnt += 1
#                 v = list_[j][1]

#     print(cnt + 1)

for tc in range(T):
    N = int(sys.stdin.readline())
    list_ = []
    for n in range(N):  # 리스트에 각 지원자의 서류심사 성적, 면접 성적 순위 저장
        st_1, st_2 = map(int, sys.stdin.readline().split())
        list_.append((st_1, st_2))

    list_.sort()  # 리스트 정렬

    v = list_[0][1]  # 1등의 면접 성적 순위를 기본값으로 저장
    cnt = 1

    for i in range(1, N):
        temp = list_[i][1]  # 1등과 2등의 면접 성적 순위부터 비교
        if temp < v:  # 1등의 순위보다 높다면 v에 새로 저장하면서 다시 반복
            v = temp
            cnt += 1

    print(cnt)
