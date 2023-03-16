# 좋다
import sys

sys.stdin = open("1253.txt")

T = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

n_list.sort()
cnt = 0

for i in range(len(n_list)):
    goal = n_list[i]
    start = 0
    end = len(n_list) - 1

    while start < end:
        sum_ = n_list[start] + n_list[end]
        if sum_ < goal:  # 계산된 값이 목표 값보다 작으면
            start += 1
        elif sum_ > goal:  # 계산된 값이 목표 값보다 크면
            end -= 1
        else:
            if start != i and end != i:  # start와 end값이 겹치지 않으면
                cnt += 1
                break
            if start == i:
                start += 1
            elif end == i:
                end -= 1

print(cnt)
