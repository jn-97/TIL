# 저울
import sys
sys.stdin = open("2437.txt")
input = sys.stdin.readline

N = int(input())
weight = list(map(int, input().split()))
weight.sort()

target = 1

for w in weight: # 1, 1, 2, 3, 6, 7, 30
    if target < w: 
        break

    target += w

print(target)