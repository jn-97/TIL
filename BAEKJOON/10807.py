# 개수 세기

m = int(input())
n = list(map(int, input().split()))
v = int(input())

cnt = 0
for i in range(len(n)):
    if n[i] == v:
        cnt += 1

print(cnt)