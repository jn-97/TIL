from pprint import pprint
import sys

sys.stdin = open('문제 21. 무방향 그래프 표현하기.txt')

N, M = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[0]*(N+1) for _ in range(N+1)] # (인접행렬) 정점의 갯수만큼 생성
graph_2 = [[] for _ in range(N+1)] # (인접리스트)

for _ in range(M):
    u, v = map(int, input().split()) # 간선의 양 끝점 u, v
    graph[u][v] = 1 # 인접 행렬
    graph[v][u] = 1 
    graph_2[u].append(v) # 인접 리스트
    graph_2[v].append(u)


pprint(graph)
print(graph_2)