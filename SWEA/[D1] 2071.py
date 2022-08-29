T = int(input())

for tc in range(1, T +1):
    a = map(int, input().split())
    b = sum(a) / 10
    print('#{} {}'.format(tc, '%.0f'%b))

    # print('#'+str(tc),'%.0f'%b)