# 최소 힙
import sys, heapq
sys.stdin = open("1927.txt")
input = sys.stdin.readline

t = int(input())

pq = []
for _ in range(t):
    x = int(input())
    
    if x == 0:
        print(heapq.heappop(pq) if pq else 0)
    else:
        heapq.heappush(pq, x)