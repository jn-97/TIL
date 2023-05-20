# 바이러스
import sys
sys.stdin = open('2606.txt')

def dfs(c):
    global ans
    ans += 1
    v[c] = 1

    for n in adj[c]:
        if not v[n]:
            dfs(n)

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

v = [0] * (N+1)
ans = 0
dfs(1)
print(ans-1)