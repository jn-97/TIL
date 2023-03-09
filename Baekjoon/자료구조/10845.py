# 큐
import sys
from collections import deque
sys.stdin = open("10845.txt")

input = sys.stdin.readline

d = deque()
for _ in range(int(input())):
    x = input().split()
    
    if x[0] == 'push':
        d.append(x[1])
    
    elif x[0] == 'pop':
        if len(d) > 0:
            print(d.popleft())
        else:
            print('-1')

    elif x[0] == 'size':
        print(len(d))

    elif x[0] == 'empty':
        if len(d) > 0:
            print('0')
        else:
            print('1')

    elif x[0] == 'front':
        if len(d) > 0:
            print(d[0])
        else:
            print('-1')

    elif x[0] == 'back':
        if len(d) > 0:
            print(d[-1])
        else:
            print('-1')