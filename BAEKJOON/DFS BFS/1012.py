# 유기농 배추
import sys
sys.stdin = open('1012.txt')

def bfs(si, sj):
    q = []
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<M and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==1:
                q.append((ni, nj))
                v[ni][nj]=1


T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*N for _ in range(M)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a][b] = 1

    v = [[0]*N for _ in range(M)]
    ans = 0

    for i in range(M):
        for j in range(N):
            if arr[i][j]==1 and v[i][j]==0:
                ans += 1
                bfs(i, j)

    print(ans)
