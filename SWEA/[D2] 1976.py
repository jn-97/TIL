import math

T = int(input())
r_h = 0
r_m = 0

for tc in range(1, T+1):
    H, M, h, m = map(int, input().split())
    r_h = ((H*60)+(h*60)+M+m)/60
    r_m = ((H*60)+(h*60)+M+m)%60
    if (math.trunc(r_h) > 12):
        r_h = (math.trunc(r_h)-12)
        print('#{} {} {}'.format(tc, math.trunc(r_h), r_m))
    else:
        print('#{} {} {}'.format(tc, math.trunc(r_h), r_m))