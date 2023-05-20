# 연결 요소의 개수
import sys
sys.stdin = open('11724.txt')

def dfs(c):
    v[c] = 1

    for n in adj[c]:
        if not v[n]:
            dfs(n)

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

v = [0] * (N+1)
ans = 0

for i in range(1, N+1):
    if v[i] == 0:
        dfs(i)
        ans += 1

print(ans)