# 와글와글 숭고한
import sys

sys.stdin = open('17388.txt')

u = list(map(int, input().split()))

sum_ = 0
min_ = 99
for i in range(len(u)):
    sum_ += u[i]
    if u[i] < min_:
        min_ = u[i]

if sum_ < 100:
    if min_ == u[0]:
        print('Soongsil')
    elif min_ == u[1]:
        print('Korea')
    else:
        print('Hanyang')
else:
    print('OK')