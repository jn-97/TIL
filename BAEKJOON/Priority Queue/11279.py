# 최대 힙
import sys, heapq
sys.stdin = open("11279.txt")
input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(N):
    x = int(input())
    if x != 0:
      heapq.heappush(pq, (-x, x))
    else:
      print(heapq.heappop(pq)[1] if pq else 0)