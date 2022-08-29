# 연속구간
from pprint import pprint 
import sys

sys.stdin = open('2495.txt')

list_ = []
for _ in range(3): 
    n = list(input())
    list_ = [[n[0]]] # 비교하기 위해 첫 번째 숫자를 저장
    ans = [1]

    cnt = 1 
    for i in range(1, 8):
        if (list_[len(list_)-1] == n[i]): 
            cnt += 1
        else: 
            list_.append(n[i])
            ans.append(cnt) # 숫자가 달라질 때마다 cnt를 ans에 저장
            cnt = 1

    ans.append(cnt) 
    print(max(ans)) # ans에서 cnt가 가장 큰 값을 출력