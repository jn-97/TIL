# 통나무 건너뛰기
import sys
sys.stdin = open("11497.txt")

T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    L = sorted(list(map(int, sys.stdin.readline().split())))
    cnt = []

    for i in range(N - 2):
        cnt.append(L[i + 2] - L[i])

    print(max(cnt))
