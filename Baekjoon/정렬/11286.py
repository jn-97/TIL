import sys
import heapq
sys.stdin = open("11286.txt")

input = sys.stdin.readline

pq = []
for _ in range(int(input())):
    x = int(input())
    
    if x: # x 가 0이 아닐 때
        heapq.heappush(pq, (abs(x), x))
    else: # x 가 0일 때
        if pq: # 비어 있지 않을 때
            print(heapq.heappop(pq)[1])
        else: # 비어 있을 때
            print(0)
        # == print(heapq.heappop(pq) if pq else 0)
