# 순회강연
import sys, heapq
sys.stdin = open('2109.txt')
input = sys.stdin.readline

n = int(input())

list_ = []
for _ in range(n):
    list_.append(list(map(int, input().split())))

list_.sort(key=lambda x: x[1])
pq = []
for i in list_:
    heapq.heappush(pq, i[0]) # p값을 pq 리스트에 삽입 

    if (len(pq) > i[1]): # 현재 d 값이 pq의 길이보다 크다면
        heapq.heappop(pq) # 가장 작은 값을 삭제

print(sum(pq))