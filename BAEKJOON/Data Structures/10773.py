# 제로
import sys
from collections import deque
sys.stdin = open("10773.txt")

input = sys.stdin.readline
d = deque()
for _ in range(int(input())):
    k = int(input())

    if k != 0:
        d.append(k)
    else:
        d.pop()

print(sum(d))