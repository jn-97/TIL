# 강의실
import sys, heapq
sys.stdin = open("1374.txt")
input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(N):
    num, start, end = map(int, input().split()) # 강의실 번호, 시작 시간, 종료 시간
    pq.append([start, end])

pq.sort()

list_ = []
heapq.heappush(list_, pq[0][1])

for i in range(1, N):
    if pq[i][0] < list_[0]: # 종료 시간보다 다음 시작 시간이 더 작으면
        heapq.heappush(list_, pq[i][1]) # 다음 종료시간을 삽입 
    else: # 종료 시간보다 다음 시작 시간이 더 크면
        print(heapq.heappop(list_)) # 가장 작은 숫자(list_[0])가 삭제됨
        heapq.heappush(list_, pq[i][1])

print(len(list_))