T = int(input())

for tc in range(1, T+1):
    n = list(map(int, input().split()))

    sum_ = 0
    for i in range(len(n)):
        if n[i]%2 != 0:
            sum_ += n[i]
        else:
            continue
    print('#{} {}'.format(tc, sum_))