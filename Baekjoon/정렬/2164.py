# 카드 2
import sys
from collections import deque
sys.stdin = open("2164.txt")
input = sys.stdin.readline

N = int(input())
d = deque()

for n in range(1, N+1):
    d.append(n)

i = 0
while len(d) > 1:
    d.popleft()
    temp = d.popleft()
    d.append(temp)
    
print(d[0])