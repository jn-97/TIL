# 시간 관리하기
import sys
sys.stdin = open("6068.txt")
input = sys.stdin.readline

works = []
for _ in range(int(input())):
    t, s = map(int, input().split())
    works.append([t, s])

works.sort(key=lambda x: x[1]) # 끝내야 하는 시간 순서대로 정렬

time = 0
limit = 0
answer = []

for i in range(len(works)):
    time += works[i][0]
    limit = works[i][1] - time
    answer.append(limit)

    if limit <= 0:
        print('-1')
        
        exit()

print(min(answer))
