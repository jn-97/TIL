# 영수증 
import sys

sys.stdin = open('25304.txt')

X = int(input()) # 총 금액
N = int(input()) # 물건 종류의 수 

sum_ = 0
for _ in range(N):
    a, b = map(int, input().split()) # 물건의 가격, 개수
    sum_ += a*b

if X == sum_:
    print('Yes')
else:
    print('No')