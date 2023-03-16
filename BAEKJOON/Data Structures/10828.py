# 스택
import sys
from collections import deque
sys.stdin = open("10828.txt")

input = sys.stdin.readline
d = deque()
for _ in range(int(input())):
    x = input().split()
    
    if x[0] == 'push':
        d.append(x[1])

    elif x[0] == 'top':
        if len(d) >  0:
            print(d[-1])
        else:
            print('-1')

    elif x[0] == 'size':
        print(len(d))
    
    elif x[0] == 'empty':
        if len(d) > 0:
            print('0')
        else:
            print('1')

    elif x[0] == 'pop':
        if len(d) > 0:
            print(d.pop())
        else:
            print('-1')

