# 두 수의 합

import sys

sys.stdin = open("3273.txt")

N = int(sys.stdin.readline())  # 수열의 크기
nums = sorted(list(map(int, sys.stdin.readline().split())))  # 수열에 포함되는 수
x = int(sys.stdin.readline())  # 두 수의 합

cnt = 0
start = 0
end = len(nums) - 1

while start < end:
    sum_ = nums[start] + nums[end]
    if sum_ < x:  # 계산된 값이 목표 값보다 작으면
        start += 1
    elif sum_ > x:  # 계산된 값이 목표 값보다 크면
        end -= 1
    else:
        cnt += 1
        start += 1
        end -= 1

print(cnt)
