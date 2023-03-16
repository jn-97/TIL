# 예산
import sys
sys.stdin = open("2512.txt")

input = sys.stdin.readline
N = int(input())
money = list(map(int, input().split()))
M = int(input())


def is_possible(mid):
    return sum(min(m, mid) for m in money) <= M

low = 0 
high = max(money)    

while low <= high:
    mid = (low + high) // 2

    if is_possible(mid): # 예산이 M 보다 작을 경우
        low = mid + 1
        ans = mid
    else: # 예산이 M 보다 클 경우
        high = mid - 1

print(ans)