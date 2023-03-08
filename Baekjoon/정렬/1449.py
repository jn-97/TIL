# 수리공 항승
import sys
sys.stdin = open("1449.txt")

input = sys.stdin.readline

N, L = map(int, input().split())
coord = [False] * 1001
for i in map(int, input().split()):
    coord[i] = True

cnt = 0
x = 0
while x < 1001:
    if coord[x]:
        cnt += 1
        x += L
    else:
        x += 1
        
print(cnt)