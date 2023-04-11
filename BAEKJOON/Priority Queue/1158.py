# 요세푸스 문제
import sys
from collections import deque

sys.stdin = open('1158.txt')

N, K = map(int, input().split())
dq = deque()

for i in range(1, N+1):
  dq.append(i)

cnt = 0
result = []
while dq:
  for i in range(K-1):
    dq.append(dq.popleft())
  result.append(dq.popleft())
  
print("<", ", ".join(map(str, result)), ">", sep='')