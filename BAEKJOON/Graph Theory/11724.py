import sys
sys.setrecursionlimit(10 ** 6)

sys.stdin = open("11724.txt")

input = sys.stdin.readline

N, M = map(int, input().split()) # 정점 N, 간선 M
adj = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))
    adj[a][b] = adj[b][a] = 1

ans = 0
chk = [False] * N # 방문체크 ex. 여러번 방문하면 안되니까 한 번 방문한 노드는 제외

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)
