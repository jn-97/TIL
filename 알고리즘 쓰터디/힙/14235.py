# 크리스마스 선물
import sys, heapq
sys.stdin = open('14235.txt')
input = sys.stdin.readline

n = int(input())

pq = []
for _ in range(n):
    a = list(map(int, input().split()))

    if a[0] == 0: # a == 0 일 경우
        if len(pq) == 0: # 아이들에게 줄 선물이 없는 경우
            print('-1') # -1 출력
        else:
            print(heapq.heappop(pq)[1])

    else:
        for i in range(1, a[0]+1):
            heapq.heappush(pq, (-a[i], a[i])) # 최대 힙
