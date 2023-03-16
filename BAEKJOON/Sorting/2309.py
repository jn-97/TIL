# 일곱 난쟁이
import sys
from itertools import combinations
sys.stdin = open("2309.txt")

input = sys.stdin.readline

doby = [int(input()) for _ in range(9)]

for i in combinations(doby, 7):
    if sum(i) == 100:
        for result in sorted(i):
            print(result)

        break # break를 걸어줘야 경우의 수가 여러개 나오지 않고 한 개만 출력했을 때 멈춘다.